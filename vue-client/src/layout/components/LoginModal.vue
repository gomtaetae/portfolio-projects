<template>
    <b-modal id="login" class="modal" hide-footer>
            <template #modal-title>
                <div class="layertit"><i class="bi bi-clipboard-check" />로그인</div>
            </template>
            <form @submit.prevent="login">
                <div class="modalcontainer">
                    <div class="loginform">
                        <label for="name"><i class="bi bi-file-person" />아이디</label>
                        <b-form-input id="name" v-model="form.name" required placeholder="이름을 입력해주세요" />
                        <label for="birthyear"><i class="bi bi-calendar-check" />비밀번호</label>
                        <b-form-input type="password" id="birthyear" v-model="form.birthyear" required placeholder="생년을 입력해주세요" />
                    </div>
                    <div class="btnwrap">
                        <b-button variant="login" type="submit">로그인</b-button>
                    </div>
                </div>
            </form>
        </b-modal>
  </template>
  
  <script>
    import axios from 'axios';


    export default {
        data() {
            return {
                form: {name: "", birthyear: ""},
            };
        },
        methods: {
            async login() {
                try {
                    console.log(this.form.name);
                    console.log(this.form.birthyear);
                    const response = await axios.post('http://' + window.location.hostname + ':5000/login_user', {
                    user_name: this.form.name,
                    birthyear: this.form.birthyear,
                });
                if (response.status === 200) {
                    console.log('로그인 성공');
                    this.$bvModal.hide('login');  // 모달 창 닫기
                    // 모달 창이 닫힌 후에 페이지 이동 처리
                    this.$nextTick(() => {
                        const currentRoute = this.$router.currentRoute;
                        if (currentRoute.path !== '/mypage') {
                            this.$router.push('/mypage');
                        }
                    });
                } else {
                    console.log('로그인 실패');
                }
                } catch (error) {
                    console.error('에러 발생:', error);
                }
            },
        },
    };
  </script>