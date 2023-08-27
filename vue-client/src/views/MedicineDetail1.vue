<!-- 간수치 술해독 -->

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
                        <strong>'간수치 술해독'</strong>에 먹으면 좋은 영양 성분을 자세하게 알려드릴게요
                    </h1>
                    &nbsp;
                    <p><strong>'글루타민'</strong>은 단백성 노폐물을 제거, 비만을 억제해줍니다.</p>
                    <p><strong>'안토시아닌'</strong>는 망막, 동공 작용촉진, 항암, 비만억제, 대사촉진을 도와주고 혈액순환에 도움을 주어 피를 맑게 해줍니다.</p>
                </div>
            </template>
            <template v-else-if="tapselect === 'bad'">
                <div class="detailTapCon">
                    <h1 class="tapcontit">
                        이런 <strong>'부작용'</strong>이 있어요.
                    </h1>
                    &nbsp;
                    <p><strong>'글루타민'</strong>은 매스꺼움, 두통, 복통, 복부 팽만감, 가벼운 피부발진, 알레르기 반응이 나옵니다.</p>
                    <p><strong>'안토시아닌'</strong>는 저혈압을 불러옵니다.</p>
                </div>
            </template>
            <template v-else-if="tapselect === 'recage'">
                <div class="detailTapCon">
                    <h1 class="tapcontit">
                        <strong>'추천 연령대'</strong> 알려드릴게요.
                    </h1>
                    &nbsp;
                    <p><strong>'글루타민'</strong>은 <strong>4050세대</strong>에게 추천드려요.</p>
                    <p><strong>'안토시아닌'</strong>은 <strong>2030세대</strong>에게 추천드려요.</p>
                </div>
            </template>
            <template v-else-if="tapselect === 'rectime'">
                <div class="detailTapCon">
                    <h1 class="tapcontit">
                        <strong>'추천 시간대'</strong> 알려드릴게요.
                    </h1>
                    &nbsp;
                    <p><strong>'글루타민'</strong>은 <strong>저녁 식사 이후</strong>에 드세요.</p>
                    <p><strong>'안토시아닌'</strong>은 <strong>저녁 식사 이후</strong>에 드세요.</p>
                </div>
            </template>
            <template v-else-if="tapselect === 'recproduct'">
                <div class="detailTapCon">
                    <h1 class="tapcontit">
                        관련 <strong>'추천 영양 제품'</strong> 안내해드릴게요.
                    </h1>
                    &nbsp;
                    <p><strong>'글루타민'</strong>은</p>
                    <p>( 제트리션 제트L글루타민프로 1500mg 180정 고함량 L-글루타민 알약 무부형제 )</p>
                    <p>- price : 39000</p>
                    <p>( 나우푸드 L 글루타민 500mg x 120캡슐 )</p>
                    <p>- price : 20500</p>
                    <p>( 쏜리서치 L-글루타민 500mg x 90캡슐 )</p>
                    <p>- price : 61000</p>
                    &nbsp;
                    &nbsp;
                    <p><strong>'안토시아닌'</strong>은</p>
                    <p>( 뉴질랜드 하이웰 빌베리 35000 60캡슐 루테인 10mg 안토시아닌 눈영양 )</p>
                    <p>- price : 87000</p>
                    <p>( 뉴질랜드 NZ100 수퍼비전 15000 60캡슐 빌베리 루테인 눈영양 안토시아닌 )</p>
                    <p>- price : 46900</p>
                    <p>( 뉴질랜드 파이오라 빌베리 50000 60캡슐 안토시아닌 루테인 눈영양 )</p>
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
                {label: "추천 영양 성분", content: "글루타민, 안토시아닌"},
                {label: "추천 조합", content: ""},
                {label: "비추 조합", content: ""},
            ],
            tapselect: "good",
        };
    },
};
</script>