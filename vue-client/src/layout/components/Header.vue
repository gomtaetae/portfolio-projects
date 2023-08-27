<template>
    <header :class="Topclass"> <!-- 메인 메뉴 고정하기-->
        <!-- 시스템 메뉴 영역 -->
        <div class = "topmenu">
            <div class = "contentbox">
                <!-- 로고 -->
                <div class = "logo">
                    <button v-on:click="goToPage('/main')">
                        <img src = "/images/logo.png" alt="이지핏 로고" />
                    </button>
                </div>
                <!-- 로그인, 회원가입 -->
                <div class = "system">
                    <button class="login" v-b-modal.login>로그인</button>
                    <button class="member" v-b-modal.member>회원가입</button>
                </div>
            </div>
        </div>


        <!-- 메인 메뉴 영역 -->
        <nav>
            <div class = "contentbox">
                <ul>
                    <li 
                        v-for="(item, index) in menulists" 
                        :key="index"
                        v-on:click="goToPage(item.link)"
                    >
                        <button v-html="item.menutext"></button>
                    </li>
                </ul>
            </div>
        </nav>
        <login-modal></login-modal>
        <b-modal id="member" class="modal" hide-footer>
            <template #modal-title>
                <div class="layertit">
                    <i class="bi bi-clipboard-check" />회원가입
                </div>
            </template>
            <div class="modalcontainer">
                <b-form @submit="Joinmember">
                    <b-form-group
                        id="formid1"
                        label="이름"
                        label-for="name"
                        description="20자 이하로만 입력하세요"
                    >
                        <b-form-input
                            id="name"
                            v-model="form.name"
                            type="text"
                            placeholder="이름을 작성해 주세요"
                            required
                        >
                        </b-form-input>
                    </b-form-group>
                    <b-form-group
                        id="formid2"
                        label="생년"
                        label-for="birthyear"
                        description="4자 숫자로만 입력하세요"
                    >
                        <b-form-input
                            id="birthyear"
                            v-model="form.birthyear"
                            type="text"
                            placeholder="태어난 년도를 작성해 주세요"
                            required
                        >
                        </b-form-input>
                    </b-form-group>
                    <b-form-group
                        id="formid3"
                        label="생일"
                        label-for="birthday"
                        description="4자리 숫자로만 입력하세요"
                    >
                        <b-form-input
                            id="birthday"
                            v-model="form.birthday"
                            type="text"
                            placeholder="태어난 날짜를 작성해 주세요"
                            required
                        >
                        </b-form-input>
                    </b-form-group>
                    <b-form-group
                        id="formid4"
                        label="성별"
                        label-for="gender"
                        description="성별을 선택해주세요"
                    >
                        <b-form-radio value="male" v-model="form.gender">남성</b-form-radio>
                        <b-form-radio value="female" v-model="form.gender">여성</b-form-radio>
                    </b-form-group>
                    
                    <!-- 관심 분야 선택하는 양식 -->
                    <b-form-group
                        id="formoid5"
                        label="관심 분야 선택"
                        label-for="checkedtype"
                        description="관심 분야를 선택하세요.(복수 선택 가능)"
                    >
                        <b-form-checkbox value="beauty" v-model="form.checkedtype">미용</b-form-checkbox>
                        <b-form-checkbox value="digestive" v-model="form.checkedtype">소화</b-form-checkbox>
                        <b-form-checkbox value="nervous" v-model="form.checkedtype">신경</b-form-checkbox>
                        <b-form-checkbox value="body" v-model="form.checkedtype">신체</b-form-checkbox>
                        <b-form-checkbox value="woman" v-model="form.checkedtype">여성</b-form-checkbox>
                        <b-form-checkbox value="circulatory" v-model="form.checkedtype">혈관</b-form-checkbox>
                    </b-form-group>
                    <div class="btnwrap half">
                        <b-button @click="join" type="submit" variant="login">확인</b-button>
                        <b-button type="reset" variant="cancel">취소</b-button>
                    </div>
                </b-form>
            </div>
        </b-modal>

    </header>
</template>


<script>
import axios from 'axios';
import LoginModal from './LoginModal.vue';
export default{
    components: {
        'login-modal': LoginModal, // 컴포넌트 등록
    },
    data() {
        return {
            menulists: [
                { menutext: "회사 소개", link: "/intro"}, 
                { menutext: "영양제 소개", link: "/medicine"},
                { menutext: "영상보기", link: "/video"},
                { menutext: "상담", link: "/counsil"},
                { menutext: "마이페이지", link: "/mypage"},
            ],
            form: {name: "", birthyear: "", birthday: "", gender: "", checkedtype: [],},
            Topclass: "",
        };
    },
    /* 스크롤 이벤트로 클래스 추가 및 삭제 */
    mounted() {
        window.addEventListener("scroll", this.handleScroll);
    },
    beforeDestroy() {
        window.removeEventListener("scroll", this.handleScroll)
    },
    methods: {
        async join() {
            try {
                const response = await axios.post('http://' + window.location.hostname + ':5000/add_user', {
                    user_name: this.form.name,
                    birthyear: this.form.birthyear,
                    birthday: this.form.birthday,
                    gender: this.form.gender,
                });
                if (response.status === 201) {
                    this.$bvModal.hide('member');  // 모달 창 닫기
                    // 모달 창이 닫힌 후에 페이지 이동 처리
                    this.$nextTick(() => {
                        const currentRoute = this.$router.currentRoute;
                        if (currentRoute.path !== '/main') {
                            this.$router.push('/main');
                        }
                    });
                } else {
                    console.log('회원가입 실패');
                }
            } catch (error) {
            console.error('에러 발생:', error);
            }
        },
        goToPage(target) {
            if (this.$router.currentRoute.path !== target) {
                this.$router.push(target);
            }
        },
        handleScroll() {console.log("scroll")},
        handleScroll() {const scrollTop = window.pageYOffset;
                        const headerTop = document.querySelector("header").clientHeight;
                        if (scrollTop < headerTop) {
                            this.Topclass = "";
                        } else {
                            this.Topclass = "scrollTop";
                        }
                    },
        Joinmember(event) {
            event.preventDefault();
            /* 회원가입이 완료되면 원래는 웹 브라우저로 넘어가야 하는데 vue에서는 만들어놓은 웹브라우저가 없으므로 알림창을 띄운다*/
            /*alert(JSON.stringify(this.form)); */
            alert("회원가입이 완료되었습니다");
            /* 회원가입을 할 때 취소를 누르면, 지금까지 입력했던 정보들 초기호하기 */
            this.$nextTick(() => {
                this.form.name = "";
                this.form.birthyear = "";
                this.form.birthday = "";
                this.form.gender = "";
                this.form.checkedtype= [];
            });
        },
    },
};
</script>