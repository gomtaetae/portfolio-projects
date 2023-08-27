<template>
  <div class="container">
    <div class="row justify-content-center">
      <div class="col-md-6">
        <div class="company-list">
          <div
            v-for="(company, index) in companies"
            :key="company.COM_ID"
            class="company-box"
          >
            <div class="company-item">
              <h3 class="company-id">{{ company["COM_ID"] }}.</h3>
              <div class="company-logo">
                <div class="circle-wrapper">
                  <img src="@/views/imgbox/common.png" alt="Company Logo" />
                </div>
              </div>
              <h2 class="company-name">회사이름 : {{ company["COM_NAME"] }}</h2>
              <p class="company-address">주소 : {{ company["HEAD_ADDRESS"] }}</p>
              <p class="company-phone">전화 번호 : {{ company["PHONE"] }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
import axios from 'axios';

export default {
  name: 'MedCompany',
  data() {
    return {
      companies: [],
    };
  },
  methods: {
    getAllCompanies() {
      let path = 'http://' + window.location.hostname + ':5000/get_all_companies';
      axios
        .get(path)
        .then((res) => {
          this.companies = res.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  created() {
    this.getAllCompanies();
  },
};
</script>

<style scoped>
.company-box {
  display: flex;
  background-color: #f9f9f9;
  margin: 10px;
  border-radius: 10px;
  box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
}

.company-item {
  padding: 20px;
  display: flex;
  flex-direction: column;
}

.company-logo {
  width: 120px; /* 아이콘 사이즈 크게 조정 */
  height: 120px; /* 아이콘 사이즈 크게 조정 */
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 50%;
  background-color: #ffffff;
  border: 1px solid #e0e0e0; /* 연한 회색 테두리 */
  box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1);
}

.circle-wrapper {
  width: 100px; /* 원 크기 조정 */
  height: 100px; /* 원 크기 조정 */
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 50%;
  background-color: #ffffff;
  border: 1px solid #e0e0e0; /* 연한 회색 테두리 */
  box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1);
}

.company-list {
  display: grid;
  grid-template-columns: repeat(2, minmax(300px, 1fr)); /* 자동 조절, 최소 300px */
  gap: 10px; /* 간격 설정 */
  justify-content: flex-start; /* 왼쪽 정렬 */
  align-items: flex-start; /* 위쪽 정렬 */
}
.circle-wrapper img {
  max-width: 100%;
  max-height: 100%;
  border-radius: 50%;
}

.company-id {
  margin-top: 10px;
  font-size: 28px; /* 아이디 숫자 크기 키우기 */
  color: #333333;
}

.company-name,
.company-address,
.company-phone {
  margin-top: 10px;
  font-size: 16px;
  color: #666666;
}
</style>