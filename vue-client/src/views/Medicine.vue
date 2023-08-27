<template>
    <Subpage :pagetit="'영양제 소개'"> <!-- 이곳에 Subpage.vue라는 공통 컴포넌트의 <slot>에 넣을 콘텐츠 영역을 <div> 태그로 작성 -->
        <div class="medicinepage">
            <VueSlickCarousel class="subpageslider" v-bind="settings" @init="handleInit" ref="carousel">
                <div class="rollimg" :class="{active: index === tabIndex}" v-for="(item, index) in Newmedicines" :key="index" @click="Clicklink(index)">
                    <span class="imgbox"><img :src="item.imgurl" /></span>
                </div>
            </VueSlickCarousel>
            
            <component
                :is="componentslist[tabIndex]"
                :medicineURL="Newmedicines[tabIndex].imgurl"
            >
            </component>
        </div>
    </Subpage>
</template>

<script>
import Subpage from "@/layout/components/Subpage.vue";
import MedicineDetail1 from "./MedicineDetail1.vue";
import MedicineDetail2 from "./MedicineDetail2.vue";
import MedicineDetail3 from "./MedicineDetail3.vue";
import MedicineDetail4 from "./MedicineDetail4.vue";



export default {
    components: {
        Subpage,
        MedicineDetail1,
        MedicineDetail2,
        MedicineDetail3,
        MedicineDetail4

    },
    mounted() {
        if (!this.$route.query.tabID) {
            this.tabIndex = 0;
        } else {
            this.tabIndex = Number(this.$route.query.tabID);
        }
    },
    data() {
        return {
            Newmedicines: [
                {imgurl:"/images/medicines_images/001.png"},
                {imgurl:"/images/medicines_images/002.png"},
                {imgurl:"/images/medicines_images/003.png"},
                {imgurl:"/images/medicines_images/004.png"},
                {imgurl:"/images/medicines_images/005.png"},
                {imgurl:"/images/medicines_images/006.png"},
                {imgurl:"/images/medicines_images/007.png"},
                {imgurl:"/images/medicines_images/008.png"},
                {imgurl:"/images/medicines_images/009.png"},
                {imgurl:"/images/medicines_images/010.png"},
                {imgurl:"/images/medicines_images/011.png"},
                {imgurl:"/images/medicines_images/012.png"},
                {imgurl:"/images/medicines_images/013.png"},
                {imgurl:"/images/medicines_images/014.png"},
                {imgurl:"/images/medicines_images/015.png"},
                {imgurl:"/images/medicines_images/016.png"},
                {imgurl:"/images/medicines_images/017.png"},
                {imgurl:"/images/medicines_images/018.png"},
                {imgurl:"/images/medicines_images/019.png"},
                {imgurl:"/images/medicines_images/020.png"},
                {imgurl:"/images/medicines_images/021.png"},
                {imgurl:"/images/medicines_images/022.png"},
                {imgurl:"/images/medicines_images/023.png"},
                {imgurl:"/images/medicines_images/024.png"},
                {imgurl:"/images/medicines_images/025.png"},
                {imgurl:"/images/medicines_images/026.png"},
            ],
            componentslist: [
                MedicineDetail1,
                MedicineDetail2,
                MedicineDetail3,
                MedicineDetail4,
            ],
            tabIndex: 0,
            settings: {
                slidesToShow: 8,
                arrows: true,
                dts: false,
                infinite: true,
                responsive: [
                    {
                        breakpoint: 1023,
                        settings: {
                            slidesToShow: 5,
                        },
                    },
                    {
                        breakpoint: 767,
                        settings: {
                            slidesToShow: 2,
                        },
                    },
                ],
            },
        };
    },
    methods: {
        Clicklink(tabIndex) {
            if (!(this.$route.query.tabId == tabIndex)) {
                this.tabIndex = tabIndex;
                return this.$router.push("/Medicine?tabId=" + tabIndex);
            }
        },
        handleInit() {
            this.$nextTick(() => {
                this.$refs.carousel.getRootNode(this.tabIndex);
            });
        },
    },
};
</script>