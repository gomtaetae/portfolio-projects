<template>
    <div class="container">
      <div class="row justify-content-center">
        <div class="col-md-6">
          <div class="medicine-list">
            <div
              v-for="(medicine, index) in medicines"
              :key="medicine.MED_ID"
              class="medicine-box"
            >
            <div class="medicine-item">
                <h3 class="medicine-id">{{ medicine["MED_ID"] }}. 제품이름 : {{ medicine["MED_NAME"] }}</h3>
            </div>
            <p class="medicine-address">가격 : {{ medicine["PRICE"] }}</p>
            <p class="medicine-phone">영양소 : {{ medicine["INGREDIENT"] }}</p>
            <p class="medicine-company">제품회사 : {{ medicine["COMPANY"] }}</p>
            <p class="medicine-deadline">유통기한 : {{ medicine["DEADLINE"] }}</p>
            <p class="medicine-shape">제품 형태 : {{ medicine["SHAPE"] }}</p>
            
            </div>
          </div>
        </div>
      </div>
    </div>
</template>
  
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'Medmedicine',
    data() {
      return {
        medicines: [],
      };
    },
    methods: {
      getAllMedicines() {
        let path = 'http://' + window.location.hostname + ':5000/get_all_medicines';
        axios
          .get(path)
          .then((res) => {
            this.medicines = res.data;
          })
          .catch((error) => {
            console.error(error);
          });
      },
    },
    created() {
      this.getAllMedicines();
    },
  };
  </script>
  
  <style scoped>
  .medicine-box {
    display: flex;
    background-color: #f9f9f9;
    margin: 10px;
    border-radius: 10px;
    box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
  }
  
  .medicine-item {
    padding: 20px;
    display: flex;
    flex-direction: column;
  }
  
  .medicine-logo {
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
  
  .medicine-list {
  display: grid;
  grid-template-columns: repeat(2, minmax(400px, 1fr)); /* Adjust the width as needed */
  gap: 10px;
  justify-content: flex-start;
  align-items: flex-start;
}
  .circle-wrapper img {
    max-width: 100%;
    max-height: 100%;
    border-radius: 50%;
  }
  
  .medicine-box {
  display: flex;
  flex-direction: column; /* Stack elements vertically */
  background-color: #f9f9f9;
  margin: 10px;
  border-radius: 10px;
  box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
}

.medicine-item {
  padding: 20px;
  /* No need for flex-direction since it's column by default */
}

.medicine-id {
  margin-top: 10px;
  font-size: 28px;
  color: #333333;
}

.medicine-name,
.medicine-address,
.medicine-phone,
.medicine-company,
.medicine-intakemethod,
.medicine-deadline,
.medicine-shape {
  margin-top: 10px;
  font-size: 16px;
  color: #666666;
}
  </style>