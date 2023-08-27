<!-- 과민성대장증후군 -->

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
                        <strong>'과민성 대장증후군'</strong>에 먹으면 좋은 영양 성분을 자세하게 알려드릴게요
                    </h1>
                    &nbsp;
                    <p><strong>'글루타치온' :</strong> ( 면역 반등, 세포 증식, 유전자 바라현, 영양소 대사 )</p>
                    <p><strong>'아연' :</strong> ( 간의 염증과 활성산소의 손상을 줄임, 철분 수송, 조기 노화 방지 및 에너시 생산 증대 )</p>
                    <p><strong>'항산화제' :</strong> ( 인체에 유해한 활성산소를 제거, 노화방지와 각종 질병예방 )</p>

                </div>
            </template>
            <template v-else-if="tapselect === 'bad'">
                <div class="detailTapCon">
                    <h1 class="tapcontit">
                        이런 <strong>'부작용'</strong>이 있어요.
                    </h1>
                    &nbsp;
                    <p><strong>'글루타치온' :</strong> ( 메스꺼움, 복통, 소화장애 )</p>
                    <p><strong>'아연' :</strong> ( 철 결핍성 빈혈, 위장장애, 메스꺼움, 구토 및 설사 )</p>
                    <p><strong>'항산화제' :</strong> ( 심혈관계 질환과 전립선암 등 일부 암 발생 위험이 증가 )</p>
                </div>
            </template>
            <template v-else-if="tapselect === 'recage'">
                <div class="detailTapCon">
                    <h1 class="tapcontit">
                        <strong>'추천 연령대'</strong> 알려드릴게요.
                    </h1>
                    &nbsp;
                    <p><strong>'아연'</strong>은 <strong>모두</strong>에게 추천드려요.</p>
                </div>
            </template>
            <template v-else-if="tapselect === 'rectime'">
                <div class="detailTapCon">
                    <h1 class="tapcontit">
                        <strong>'추천 시간대'</strong> 알려드릴게요.
                    </h1>
                    &nbsp;
                    <p><strong>'아연'</strong>은 <strong>아침 식사 이전</strong>에 드세요.</p>
                    <p><strong>'항산화제'</strong>은 <strong>아침 식사 이전</strong>에 드세요.</p>
                </div>
            </template>
            <template v-else-if="tapselect === 'recproduct'">
                <div class="detailTapCon">
                    <h1 class="tapcontit">
                        관련 <strong>'추천 영양 제품'</strong> 안내해드릴게요.
                    </h1>
                    &nbsp;
                    <p><strong>'글루타치온'</strong></p>
                    <p>( GLUTATHIONE글루타티온 영양제 )</p>
                    <p>- price : 39000</p>
                    <p>( 줄리스초이스 글루타티온 분말 가루 스틱 )</p>
                    <p>- price : 20500</p>
                    <p>( 글루타치온 1000mg 6개월분 글로타치온 클루타치온 글루타치온효과효능 글루타티온 )</p>
                    <p>- price : 61000</p>
                    &nbsp;
                    &nbsp;
                    <p><strong>'아연'</strong></p>
                    <p>( 닥터스베스트 알파리포산 300 300mg 베지캡슐 180정 )</p>
                    <p>- price : 87000</p>
                    <p>( 칼슨랩스 칼슨랩 글루타치온 부스터 알파 리포산 180 캡슐 Carlson Labs )</p>
                    <p>- price : 20100</p>
                    &nbsp;                   
                    &nbsp;
                    <p><strong>'항산화제'</strong></p>
                    <p>( 에스더 항산화제 코엔자임Q10 )</p>
                    <p>- price : 87000</p>
                    <p>( 토마토라이코펜 )</p>
                    <p>- price : 46900</p>
                    <p>( 라이코마토 )</p>
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
                {label: "추천 영양 성분", content: "글루타치온, 아연, 항산화제"},
                {label: "추천 조합", content: "글루타치온-비타민B : 미백효과와 함께 피부가 좋아진다"},
                {label: "비추 조합", content: "아연-철분, 아연-칼슘 : 서로의 흡수를 방해한다 / 아연-항생제 : 화합물을 형성해 흡수를 방해한다"},
            ],
            tapselect: "good",
        };
    },
};
</script>