<!-- 소화불량 -->

<template>
    <section class="medicinedetail">
        <!-- 영양 성분 기본 정보-->
        <h1 class="medicinetitle">
            Health Care, 여러분의 건강을 책임지겠습니다
            <span>증상에 따른 영양 성분부터, 조합, 그리고 시간대 및 연령대 별로 추천해주는 Health Care.</span>
        </h1>
        &nbsp;
        <div class="medicine-info">
            <!--이미지가 들어갈 div-->
            <div class="imgview">
                <div class="imgmedicine"><img :src="medicineURL" alt="" /></div>
            </div>
            <!--기본 정보가 들어갈 div-->
            <div class="infolist">
                <ul>
                    <li v-for="(item, index) in medicineinfolists" :key="index">
                        <span class="label" v-html="item.label"></span>
                        <span class="infocontent" v-html="item.content"></span>
                    </li>
                </ul>
            </div>
        </div>
        <!-- 상세 탭 메뉴 div -->
        <div class="medicine-detailinfo">
            <!--영양성분 상세 탭 메뉴 영역-->
            <div class="detailTap">
                <b-form-radio name="detail-tap" v-model="tapselect" value="good" button button-variant="detailtap">
                    <i class="bi bi-plus-circle" />효능
                </b-form-radio>
                <b-form-radio name="detail-tap" v-model="tapselect" value="bad" button button-variant="detailtap">
                    <i class="bi bi-dash-circle" />부작용
                </b-form-radio>
                <b-form-radio name="detail-tap" v-model="tapselect" value="recage" button button-variant="detailtap">
                    <i class="bi bi-person-add" />추천 연령대
                </b-form-radio>
                <b-form-radio name="detail-tap" v-model="tapselect" value="rectime" button button-variant="detailtap">
                    <i class="bi bi-clock" />추천 시간대
                </b-form-radio>
                <b-form-radio name="detail-tap" v-model="tapselect" value="recproduct" button button-variant="detailtap">
                    <i class="bi bi-capsule" />추천 영양 제품
                </b-form-radio>
            </div>
            <!--영양성분 상세 콘텐츠 영역-->
            <template v-if="tapselect === 'good'">
                <div class="detailTapCon">
                    <h1 class="tapcontit">
                        <strong>'소화불량'</strong>에 먹으면 좋은 영양 성분을 자세하게 알려드릴게요
                    </h1>
                    &nbsp;
                    <p><strong>'비오틴' :</strong> ( 고혈압 및 대사증후군을 억제, 인슐린 저항성을 낮추는 효과 )</p>
                    <p><strong>'유산균' :</strong> ( 고혈압 및 대사증후군을 억제, 인슐린 저항성을 낮추는 효과 )</p>
                    <p><strong>'마키베리' :</strong> ( 음식물을 소화시켜 영양분의 흡수를 도와준다. )</p>

                </div>
            </template>
            <template v-else-if="tapselect === 'bad'">
                <div class="detailTapCon">
                    <h1 class="tapcontit">
                        이런 <strong>'부작용'</strong>이 있어요.
                    </h1>
                    &nbsp;
                    <p><strong>'비오틴' :</strong> ( 메스꺼움, 복통, 소화장애 )</p>
                    <p><strong>'유산균' :</strong> ( 근육 쇠약, 피로, 메스꺼움 및 설사 )</p>
                    <p><strong>'마키베리' :</strong> ( 심혈관계 질환과 전립선암 등 일부 암 발생 위험이 증가 )</p>
                </div>
            </template>
            <template v-else-if="tapselect === 'recage'">
                <div class="detailTapCon">
                    <h1 class="tapcontit">
                        <strong>'추천 연령대'</strong> 알려드릴게요.
                    </h1>
                    &nbsp;
                    <p><strong>'비오틴'</strong>은 <strong>2030세대</strong>에게 추천드려요.</p>
                    <p><strong>'유산균'</strong>은 <strong>모두</strong>에게 추천드려요.</p>
                    <p><strong>'마키베리'</strong>은 <strong>모두</strong>에게 추천드려요.</p>

                </div>
            </template>
            <template v-else-if="tapselect === 'rectime'">
                <div class="detailTapCon">
                    <h1 class="tapcontit">
                        <strong>'추천 시간대'</strong> 알려드릴게요.
                    </h1>
                    &nbsp;
                    <p><strong>'유산균'</strong>은 <strong>아침 식사 이전</strong>에 드세요.</p>
                    <p><strong>'마키베리'</strong>은 <strong>저녁 식사 이후</strong>에 드세요.</p>
                </div>
            </template>
            <template v-else-if="tapselect === 'recproduct'">
                <div class="detailTapCon">
                    <h1 class="tapcontit">
                        관련 <strong>'추천 영양 제품'</strong> 안내해드릴게요.
                    </h1>
                    &nbsp;
                    <p><strong>'비오틴'</strong></p>
                    <p>( 메디타민 비오틴10000 맥주효모 영양제 비타민B 판토텐산 )</p>
                    <p>- price : 39000</p>
                    <p>( 판토모나 비오틴 복합 관리 영양제 )</p>
                    <p>- price : 20500</p>
                    <p>( 나우푸드 비오틴 10000mcg / 10mg 120캡슐 [4개월분 + 4개월분] )</p>
                    <p>- price : 61000</p>
                    &nbsp;
                    &nbsp;
                    <p><strong>'유산균'</strong></p>
                    <p>( 유한양행 와이즈바이옴 마이크로바이옴 유산균 패밀리 에스 4개월 )</p>
                    <p>- price : 87000</p>
                    <p>( 덴프스 덴마크 유산균 이야기 170mg )</p>
                    <p>- price : 20100</p>
                    &nbsp;                   
                    &nbsp;
                    <p><strong>'마카베리'</strong></p>
                    <p>( 익스트림 김종국 블랙마카 1800 6통 (6개월분) )</p>
                    <p>- price : 87000</p>
                    <p>( 광동 블랙마카365 100% 페루산 x 6개월 )</p>
                    <p>- price : 46900</p>
                    <p>( 나우푸드 로우 마카 750mg x 90베지캡슐 )</p>
                    <p>- price : 20100</p>
                    &nbsp;
                    <p>등이 있습니다.</p>
                </div>
            </template>
        </div>
    </section>
</template>

<script>
export default {
    props: ['medicineURL'],
    data() {
        return {
            medicineinfolists:[
                {label: "목적", content: "소화"},
                {label: "추천 영양 성분", content: "비오틴, 유산균, 마카베리"},
                {label: "추천 조합", content: "비오틴-종합비타민: 탈모, 모발, 네일에 좋다"},
                {label: "비추 조합", content: "유산균-항생제: 항생제는 좋은 균인 유산균도 함께 죽여 약효를 감소시키고 유산균의 효능을 떨어트림"},
            ],
            tapselect: "good",
        };
    },
};
</script>