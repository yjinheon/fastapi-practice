// 전역적으로 사용 할 수 있도록 plugin으로 등록
import 'bootstrap/dist/css/bootstrap.css';
import { createApp } from "vue";
import axios from 'axios';

import App from './App.vue';
import router from './router';

// Every Vue application starts by creating a new Vue instance with the Vue function:

const app = createApp(App).use(router); // router를 app에 등록

axios.defaults.withCredentials = true;
axios.defaults.baseURL = 'http://localhost:5000/';  // the FastAPI backend


// 옵션속성

// 옵션 속성은 인스턴스를 생성할 때 재정의할 data, el, template 등의 속성을 의미

//     el : 뷰로 만든 화면이 그려지는 시작점을 의미, 뷰 인스턴스로 화면을 렌더링할 때 화면이 그려질 위치의 돔 요소를 지정해 주어야 한다.
//     template : 화면에 표시할 HTML, CSS 등의 마크업 요소를 정의하는 속성
//     methods : 화면 로직 제어와 관계된 메서드를 정의하는 속성
//     created : 뷰 인스턴스가 생성되자마자 실행할 로직을 정의할 수 있는 속성




app.use(router);
app.mount("#app"); // id 가 app 인 tag에 vue app을 mount

// index.html의 div id="app" 에 app instance가 렌더링 됨


// beforeCreate : 인스턴스가 생성되고 나서 가장 처음으로 실행되는 라이프 사이클 단계, data 속성과 method 속성이 아직 인스턴스에 정의되어 있지 않음. 화면 요소에도 접근 불가
// created : beforeCreate 라이프 사이클 단계 다음에 실행되는 단계, data 속성과 method 속성에 정의된 값에 접근하여 로직을 실행할 수 있지만, 아직 인스턴스가 화면 요소에 부착되지 전이기 때문에 template 속성에 정의된 돔 요소로 접근 불가, 컴포넌트가 생성되고 나서 실행되는 단계이기 때문에 서버에 데이터를 요청하여 받아오는 로직을 수행하기 좋음.
// beforeMount : created 단계 이후 template 속서에 지정한 마크업 속성을 render() 함수로 변환한 후 el 속성에 지정한 화면 요소에 인스턴스를 부착하기 전에 호출되는 단계, render()함수가 호출되기 직전의 로직을 추가하기 좋음
// mounted : el 속성에서 지정한 화면 요소에 인스턴스가 부착되고 나면 호출되는 단계, 화면 요서에 접근이 가능하여 제어를 하는 로직을 수행하기 좋음.
// beforeUpdate : el 속성에서 지정한 화면 요소에 인스턴스가 부착되고 나면 인스턴스에 정의한 속성들이 화면에 치환됨. 치환된 값은 뷰의 반응성을 제공하기 위해 $watch 속성으로 감시함. 이를 데이터 관찰이라함. 관찰하고 있는 데이터가 변경되면 가상 돔으로 화면을 다시 그리기 전에 호출되는 단계, 변경 예정인 새 데이터에 접근할 수 있어 변경 예정 데이터의 값과 관련된 로직을 미리 넣을 수 있음.
// updated : 데이터가 변경되고 나서 가상 돔으로 다시 화면을 그리고 나면 실행되는 단계, 데이터 변경 후 화면 요소 제어와 관련된 로직을 추가하기 좋은 단계
// beforeDestroy : 뷰 인스턴스가 파괴되기 직전에 호출되는 단계, 아직 인스턴스에 접근 가능, 뷰 인스턴스의 데이터를 삭제하기 좋은 단계
// destoryed : 뷰 인스턴스가 파괴되고 나서 후출되는 단계, 뷰 인스턴스에서 정의한 모든 속성이 제거되고 하위에 선언한 인스턴스들 또한 모두 파괴됨
