from fastapi import FastAPI, HTTPException
from tortoise.exceptions import DoesNotExist

from src.database.models import Notes
from src.schemas.notes import NoteOutSchema
from src.schemas.token import Status

# async : 비동기 함수
# await : 비동기 함수를 호출할 때 사용

async def get_notes():
    return await NoteOutSchema.from_queryset(Notes.all())

async def get_note(note_id) -> NoteOutSchema:
    return await NoteOutSchema.from_queryset_single(Notes.get(id=note_id))

async def create_note(note,current_user):
    # exclude_unset=True 기본적으로 partial update를 위해 사용.
    # request에서 받은 요청 중 item의 초기값을 제외한 입력값만 추려서 dict를 구성해줌
    note_dict = note.dict(exclude_unset=True)
    note_dict["author_id"] = current_user.id
    note_obj = await Notes.create(**note_dict)

    return await NoteOutSchema.from_tortoise_orm(note_obj)

async def update_note(note_id, note, current_user) -> NoteOutSchema:
    try:
        db_note = await NoteOutSchema.from_queryset_single(Notes.get(id=note_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"Note {note_id} not found")

    if db_note.author_id == current_user.id:
        await Notes.filter(id=note_id).update(**note.dict(exclude_unset=True)) # exclude_unset=True 기본적으로 partial update를 위해 사용.
        return await NoteOutSchema.from_queryset_single(Notes.get(id=note_id)) # from_queryset_single: 하나의 객체를 반환
    raise HTTPException(status_code=403, detail=f"Not authorized to update")

async def delete_note(note_id, current_user) -> Status:
    try:
        db_note = await NoteOutSchema.from_queryset_single(Notes.get(id=note_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"Note {note_id} not found")

    if db_note.author_id == current_user.id:
        deleted_count = await Notes.filter(id=note_id).delete()
        if not deleted_count:
            raise HTTPException(status_code=404, detail=f"Note {note_id} not found")
        return Status(message=f"Deleted note {note_id}")

    raise HTTPException(status_code=403, detail=f"Not authorized to delete")