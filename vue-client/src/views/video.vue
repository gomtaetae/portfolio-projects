<template>
    <Subpage :pagetit="'영상보기'">
        <div class="videopage">
            <div class="subpageguide">
                각종 영양 성분과 관련된 영상들을 시청하실 수 있습니다.
            </div>
            <listComm :lists="lists" />
        </div>
    </Subpage>
</template>

<script>
import Subpage from "@/layout/components/Subpage.vue";
import listComm from "@/layout/components/listComm.vue";
export default {
    components: {Subpage, listComm},
    data() {
        return {
            lists: [
                {
                    img: "/images/youtube1.png",
                    title: "영양제 여러개 먹기 부담스러우시면 종합비타민 '이걸' 드시면 됩니다.",
                    date: "2022.06.24",
                    dec: "약사가 들려주는 약이야기. <br /> 국내용 종합비타민 추천 영상입니다. 국내는 건강기능식품 허가 사항 때문에 성분에 대한 제약이 많아서 직구 대비 신경써야하는 사항들이 적습니다. 최근에 다양한 제품들이 많이 나오고 있으니 참고하시면 좋을 것 같습니다.",
                    link: "https://www.youtube.com/watch?v=9JBaSCxRgAg"
                },
                {
                    img: "/images/youtube2.png",
                    title: "약사가 직접 섭취해본 가성비 좋은 유산균부터~ 최고 품질의 유산균까지 총정리 해봤습니다. (좋은 유산균을 직접 고르는 기준!까지)",
                    date: "2023.05.06",
                    dec: "약사가 들려주는 약이야기. <br /> 시중에 나와있는 수많은 유산균들 중에서 가장 좋은 유산균이 무엇일지 생각해봤습니다. 유산균은 고르는 기준을 정하셔야합니다. 직접 챙겨먹은 유산균을 바탕으로 리뷰했으니, 참고하셔서 몸에 맞는 유산균 꼭 챙기시길 바랍니다.",
                    link: "https://www.youtube.com/watch?v=Fz7raO50gsE"
                },
                {
                    img: "/images/youtube3.png",
                    title: "골다공증에 필수 영양제 2가지, 꼭 먹어야 하는 이유는? / 서울백병원 가정의학과 박현아",
                    date: "2023.03.05",
                    dec: "의학채널 비온뒤. <br /> 많은 사람들이 겪는 골다골증, 그에 대한 오해도 많습니다. 골다공증에 좋은 영양제부터 골다공증에 대한 잘못된 편견까지! 영상을 보면서 그 궁금증 다 풀고 가세요!",
                    link: "https://www.youtube.com/watch?v=78hLERBud8g"
                },
            ],
        };
    },
};
</script>