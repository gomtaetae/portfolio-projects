<template>
  <div class="map-container">
    <h1>Google Map in Vue</h1>
    <GmapMap
      :center="center"
      :zoom="19"
      style="width: 70%; height: 400px;"
    >
      <GmapMarker :position="center" />
    </GmapMap>
    <div class="directions-box">
      <div class="directions-title">찾아오시는 길</div><br>
      <p class="directions-sub">도보이용시 </p> <p class="directions-end">혜화역 4번 출구, 베스킨라빈스 큰 길로 쭈욱 따라 들어오면 좌측에 국민은행, 그 우측 골목으로 요겐후르츠 가게를 끼고 좁은 골목의 좌측 지하에 있습니다.</p><br>
      <p class="directions-sub">대중교통 이용시 </p> <p class="directions-end">1. 지하철 이용시 혜화혁 4호선을 이용하시고 도보이용시 안내사항을 참고하시면 됩니다.<br><br>2. 버스 이용시 151, 171, 172, 272, 601 버스를 이용하시면 됩니다.<br> <br>3. 자차 이용시 CGV 주차장 혹은 건물 내 주차장을 이용하시면 됩니다. 건물내 주차장은 협소하오니 대중교통 이용을 추천드립니다.</p>
      <!-- 이곳에 필요한 추가 정보나 링크를 포함시킬 수 있습니다. -->
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      center: { 
        lat: 37.58369827270508,
        lng: 126.99989318847656 
      }, // 초기 맵 중심 좌표
    };
  },
};
</script>

<style>
.map-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
}

.directions-box {
  margin-top: 20px;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
  background-color: #f5f5f5;
  width: 70%; /* 가로 길이를 맵과 같게 설정 */
  text-align: left;
}

.directions-title {
  font-size: 30px; /* 글자 크기 설정 */
}

.directions-sub {
  font-size: 20px;
}

.directions-end {
  font-size: 15px;
}
</style>