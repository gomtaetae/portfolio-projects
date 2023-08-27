<template>
  <div class="mypage">
    <h1>My Page</h1>
    <div class="user-info" >
      <p class="info-line"><i class="bi bi-person"></i><strong>이름 :</strong>    <span class="user-info-text">{{ userInfo["USER_NAME"] }}</span></p>
      <p class="info-line"><i class="bi bi-123"></i><strong>나이 :</strong>     <span class="user-info-text">{{ calculateAge(userInfo["BIRTHYEAR"]) }}</span></p>
      <p class="info-line"><i class="bi bi-balloon-heart"></i><strong>생년 :</strong>     <span class="user-info-text">{{ userInfo["BIRTHYEAR"] }}</span></p>
      <p class="info-line"><i class="bi bi-balloon-heart-fill"></i><strong>생일 :</strong>     <span class="user-info-text">{{ userInfo["BIRTHDAY"] }}</span></p>
      <p class="info-line"><i class="bi bi-gender-ambiguous"></i><strong>성별 :</strong>     <span class="user-info-text">{{ userInfo["GENDER"] }}</span></p>
  </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      userInfo: { }
    };
  },
  created() {
  this.fetchUserInfo(); // 컴포넌트 생성시 회원 정보 가져오기
  },
  methods: {
      calculateAge(birthyear) {
          const currentYear = new Date().getFullYear();
          return currentYear - birthyear;
      },
      async fetchUserInfo() {
      
          try {
              const response = await axios.get('http://' + window.location.hostname + ':5000/get_user/4'); // 사용자 정보 가져오는 엔드포인트로 변경

              if (response.status === 200) {
                  this.userInfo = response.data[0]; // 첫 번째 사용자 정보를 userInfo에 저장
              } else {
                  console.log('회원 정보 가져오기 실패');
              }
          } catch (error) {
              console.error('에러 발생:', error);
          }
      }
  }
};
</script>

<style scoped>
.mypage > h1 {
    text-align: center;
    margin-top: 20px;
    font-size: 40px;
    font-family: '맑은고딕';
}

.info-line {
  font-size: 18px;
  padding: 20px 0;
  padding-left: 10px;
}

.user-info {
  border: 1px solid #ccc;
  padding: 20px;
  margin-top: 10px;
  text-align: left; /* 왼쪽 정렬 */
  }

.user-info-text {
  font-size: 18px; /* 이름과 사용자 정보 크기 조절 */
  }

.info-line {
  margin-bottom: 10px; /* 각 줄 간격 벌리기 */
  }
</style>
