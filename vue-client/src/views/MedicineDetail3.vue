<!-- 변비 -->

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
                        <strong>'변비'</strong>에 먹으면 좋은 영양 성분을 자세하게 알려드릴게요
                    </h1>
                    &nbsp;
                    <p><strong>'골다공증약' :</strong> ( 면역 반등, 세포 증식, 유전자 바라현, 영양소 대사 )</p>
                    <p><strong>'아스피린' :</strong> ( 간의 염증과 활성산소의 손상을 줄임, 철분 수송, 조기 노화 방지 및 에너시 생산 증대 )</p>
                </div>
            </template>
            <template v-else-if="tapselect === 'bad'">
                <div class="detailTapCon">
                    <h1 class="tapcontit">
                        이런 <strong>'부작용'</strong>이 있어요.
                    </h1>
                    &nbsp;
                    <p><strong>'골다공증약' :</strong> ( 점막조직의 괴사, 식도와 위장의 손상,발진 그리고 턱뼈가 썩는 악골괴사 )</p>
                    <p><strong>'아스피린' :</strong> ( 손과 발에 멍이 쉽게 듭니다. 속쓰림, 위장 불량 )</p>
                </div>
            </template>
            <template v-else-if="tapselect === 'recage'">
                <div class="detailTapCon">
                    <h1 class="tapcontit">
                        <strong>'추천 연령대'</strong> 알려드릴게요.
                    </h1>
                    &nbsp;
                    <p><strong>'아스피린'</strong>은 <strong>모두</strong>에게 추천드려요.</p>
                </div>
            </template>
            <template v-else-if="tapselect === 'rectime'">
                <div class="detailTapCon">
                    <h1 class="tapcontit">
                        <strong>'추천 시간대'</strong> 알려드릴게요.
                    </h1>
                    &nbsp;
                    <p><strong>'아스피린'</strong>은 <strong>아침 식사 이전</strong>에 드세요.</p>
                </div>
            </template>
            <template v-else-if="tapselect === 'recproduct'">
                <div class="detailTapCon">
                    <h1 class="tapcontit">
                        관련 <strong>'추천 영양 제품'</strong> 안내해드릴게요.
                    </h1>
                    &nbsp;
                    <p><strong>'골다공증약'</strong></p>
                    <p>( 커클랜드 아스피린 81mg )</p>
                    <p>- price : 39000</p>
                    <p>( 바이엘 아스피린 bayer 325 mg 500정 )</p>
                    <p>- price : 20500</p>
                    &nbsp;
                    &nbsp;
                    <p><strong>'아스피린'</strong></p>
                    <p>( 솔라레이 화란 국화 피버퓨 455mg 베지캡슐 100정 )</p>
                    <p>- price : 87000</p>
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
                {label: "추천 영양 성분", content: "골다공증약, 아스피린"},
                {label: "추천 조합", content: "아스피린-칼슘 : 고혈압에 좋다"},
                {label: "비추 조합", content: "아스피린-인 : 서로의 흡수를 방해한다"},
            ],
            tapselect: "good",
        };
    },
};
</script>