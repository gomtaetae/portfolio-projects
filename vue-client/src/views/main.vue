<!-- 메인 콘텐츠는 index.vue의 <router-view>에 출력 -->

<template>
    <section class = "maincontents">


        <section class="mainindicators">
            <VueSlickCarousel class="subpageslider" @init="handleInit" ref="carousel">
                <div class="rollimg">
                    <div class="carousel-inner">
                        <div class="carousel-item active">
                            <img src="/images/mainimg.png" class="d-block w-100" alt="..." />
                        </div>
                        <div class="carousel-item">
                            <img src="/images/mainimg.png" class="d-block w-100" alt="..." />
                        </div>
                        <div class="carousel-item">
                            <img src="zombie3.jpg" class="d-block w-100" alt="..." />
                        </div>
                    </div>
                    <button class="carousel-control-prev" type="button" data-bs-target="#carouselExample" data-bs-slide="prev">
                        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                        <span class="visually-hidden">Previous</span>
                    </button>
                    <button class="carousel-control-next" type="button" data-bs-target="#carouselExample" data-bs-slide="next">
                        <span class="carousel-control-next-icon" aria-hidden="true"></span>
                        <span class="visually-hidden">Next</span>
                    </button>
                </div>
            </VueSlickCarousel>
        </section>



        <!--
        <section class="mainbanner"><img src="/images/mainimg.png" /></section>
        -->
        
        <div class="jb-division-line"></div>
        
        <section class="newmedicine">   
            <h1 class="maintit">
                <p1> -     Health Care에서 다루고 있는 증상들     -</p1>
            </h1>
            <div class="tapcontent">
                <div class="tap">
                    <b-button variant="tap active" @click="AddContents('Newmedicines_digestive')">소화</b-button>
                    <b-button variant="tap" @click="AddContents('Newmedicines_woman')">여성</b-button>
                    <b-button variant="tap" @click="AddContents('Newmedicines_beauty')">미용</b-button>
                    <b-button variant="tap" @click="AddContents('Newmedicines_nervous')">신경</b-button>
                    <b-button variant="tap" @click="AddContents('Newmedicines_circulatory')">혈관</b-button>
                    <b-button variant="tap" @click="AddContents('Newmedicines_body')">신체</b-button>
                </div>
                <VueSlickCarousel class="mainslider" v-bind="settings">
                    <div class="rolling" v-for="(item, index) in Newmedicines" :key="index">
                        <span class="imgbox"><img :src="item.imgurl" /></span>
                    </div>
                </VueSlickCarousel>
            </div>
        </section>


        <div class="jb-division-line"></div>

        <section class="mainbannermenu">
            <body>
                <div class="bodyNav">
                    <div class="card">
                        <img src="./imgbox/banner_icon1.png" class="card-img-top" alt="...">
                        <div class="card-body">
                            <h5 class="card-title" style="font-size: 30px;">영양 성분별</h5>
                            <p class="card-text">성분을 알고 싶다면?</p>
                            <a href="/medicine" class="btn btn-primary">보러가기</a>
                        </div>
                    </div>
                    <div class="card">
                        <img src="./imgbox/banner_icon2.png" class="card-img-top" alt="...">
                        <div class="card-body">
                            <h5 class="card-title" style="font-size: 30px;">영상보기</h5>
                            <p class="card-text">전문가의 말을 구체적으로 듣기</p>
                            <a href="/video" class="btn btn-primary">보러가기</a>
                        </div>
                    </div>
                    <div class="card">
                        <img src="./imgbox/banner_icon3.png" class="card-img-top" alt="...">
                        <div class="card-body">
                            <h5 class="card-title" style="font-size: 30px;">1:1 퍼스널 상담</h5>
                            <p class="card-text">전문가에게 상의학고 싶다면?</p>
                            <a href="/counsil" class="btn btn-primary">보러가기</a>
                        </div>
                    </div>
                </div>
            </body>
        </section>
    

        <!-- <section class="searchmedicine">
            <h1 class="maintit">
                성분 검색<span>찾고자 하는 성분명을 검색해주세요</span>
            </h1>
            <div class="inputarea">
                <b-form-input />
                <b-button variant="search"><i class="bi bi-search"></i></b-button>
                <div class="autolayer">
                    <ul>
                        <li></li>
                    </ul>
                </div>
            </div>
            <div class="guidehash">
                <span
                    v-for="(item, index) in hashdata"
                    :key="index"
                    v-html="item.text"
                ></span>
            </div>
        </section>  -->

        
    </section>
</template>


<script>
import { BIconEaselFill } from 'bootstrap-vue';

export default{
    data() {
        return {
            Newmedicines: [],
            Newmedicines_digestive: [
                {imgurl:"/images/medicines_images/001.png"},
                {imgurl:"/images/medicines_images/002.png"},
                {imgurl:"/images/medicines_images/003.png"},
                {imgurl:"/images/medicines_images/004.png"},
                {imgurl:"/images/medicines_images/005.png"},
            ],
            Newmedicines_woman: [
                {imgurl:"/images/medicines_images/006.png"},
                {imgurl:"/images/medicines_images/007.png"},
                {imgurl:"/images/medicines_images/008.png"},
            ],
            Newmedicines_beauty: [
                {imgurl:"/images/medicines_images/009.png"},
                {imgurl:"/images/medicines_images/010.png"},
                {imgurl:"/images/medicines_images/011.png"},
                {imgurl:"/images/medicines_images/012.png"},
                {imgurl:"/images/medicines_images/013.png"},
            ],
            Newmedicines_nervous: [
                {imgurl:"/images/medicines_images/014.png"},
                {imgurl:"/images/medicines_images/015.png"},
                {imgurl:"/images/medicines_images/016.png"},
                {imgurl:"/images/medicines_images/017.png"},
                {imgurl:"/images/medicines_images/018.png"},
            ],
            Newmedicines_circulatory: [
                {imgurl:"/images/medicines_images/019.png"},
                {imgurl:"/images/medicines_images/020.png"},
                {imgurl:"/images/medicines_images/021.png"},
                {imgurl:"/images/medicines_images/022.png"},
            ],
            Newmedicines_body: [
                {imgurl:"/images/medicines_images/023.png"},
                {imgurl:"/images/medicines_images/024.png"},
                {imgurl:"/images/medicines_images/025.png"},
                {imgurl:"/images/medicines_images/026.png"},
            ],
            settings: {
                slidesToShow: 5, //화면에 나타날 슬라이드 개수
                arrows: true,    //버튼 사용 여부
                dots: false,     //하단 버튼 사용 여부
                infinite: true,  //
                responsive: [
                    {
                        breakpoint: 767,    // 브라우저 크기가 767 이하일 때
                        settings: {
                            slidesToShow: 4,
                        },
                    },
                    {
                        breakpoint: 414,    // 브라우저 크기가 464 이하일 때
                        settings: {
                            slidesToShow: 2,
                        },
                    },
                ],
            },
            hashdata: [
                { text: "소화", value: "소화"},
                { text: "여성", value: "여성"},
                { text: "미용", value: "미용"},
                { text: "신경", value: "신경"},
                { text: "혈관", value: "혈관"},
                { text: "신체", value: "신체"},

            ],
            mainbanner: [
                {
                    stitle : "성분을 알고 싶다면?",
                    maintit : "영양 성분별",
                    iconname : "bi-stickies",
                    url: "/medicine"
                },
                {
                    stitle : "전문가의 말을 구체적으로 듣기",
                    maintit : "영상보기",
                    iconname : "bi-stickies",
                    url: "/video"
                },
                {
                    stitle : "전문가에게 상의하고 싶다면?",
                    maintit : "1:1 퍼스널 상담",
                    iconname : "bi-stickies",
                    url: "/counsil"
                },
            ],
        };
    },
    created() {
        this.Newmedicines = this.Newmedicines_digestive;
    },
    methods: {
        AddContents(contents) {
            this.Newmedicines = this[contents];
            document.querySelector(".active").classList.remove("active");
            event.target.classList.add("active")
        },
        gotoPage(url) {
            if(url == "/medicine") {
                this.$router.push(url);
            }
            else {
                window.open(url, "_blank"); // 전달받은 매게변수에 따라서 내부로 이동은 라우터 변경으로 작성, 외부로 이동하는 링크는 window.open()을 이용하여 작성
            }
        },
    },
};
</script>

<style>
   
  
    .main-container {
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        align-items: center;
        min-height: 100vh;
    }

    .bodyNav {
        display: flex; 
        justify-content: center; 
        align-items: center; 
        flex-wrap: wrap;
        margin-top: 50px;
    }

    .card {
        width: 18rem;
        margin: 0 20px 20px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }

    .card-img-top {
        height: auto;
        width: auto;
        object-fit: fill;
        max-width: 200px;
        max-height: 200px;
        display: block; margin: 0px auto;
        padding: 10%;
    }

</style>