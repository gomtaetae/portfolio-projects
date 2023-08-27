<template>
    <Subpage :pagetit="'1:1 상담 신청 폼'">
        <div class="classsample">
            <div class="subpageguide">
                1:1 퍼스널 상담을 진행하고 있습니다. <br /> Health Care에서 본인 맞춤 영양제 케어를 받고 싶으신 분들은 아래 내용대로 접수해주세요.
            </div>
        </div>
        <b-form @submit="Classcall">
            <b-form-group id="reason" label="신청 이유" label-for="reason" description="신청 이유를 작성해 주세요.">
                <b-form-input id="reason" v-model="form.reason" type="text" required>
                </b-form-input>
            </b-form-group>

            <!-- 원하는 선생님 선택하는 양식 -->
            <b-form-group id="teacher" label="원하는 선생님" label-for="checkedtype" description="원하는 선생님을 선택해 주세요.">
                <b-form-checkbox value="A" v-model="form.checkedtype">방형욱 교수님</b-form-checkbox>
                <b-form-checkbox value="B" v-model="form.checkedtype">강형욱 선생님</b-form-checkbox>
                <b-form-checkbox value="C" v-model="form.checkedtype">전창민 반장님</b-form-checkbox>
                <b-form-checkbox value="D" v-model="form.checkedtype">정용준 디비장</b-form-checkbox>
            </b-form-group>

            <b-form-group id="formname" label="이름" label-for="formname" description="본인 이름을 작성해 주세요.">
                <b-form-input id="formname" v-model="form.formname" type="text" required>
                </b-form-input>
            </b-form-group>
            <b-form-group id="formphone" label="연락처" label-for="formphone" description="연락이 가능한 번호를 입력해주세요.(-제외))">
                <b-form-input id="formphone" v-model="form.formphone" type="text" required>
                </b-form-input>
            </b-form-group>
            <b-form-group id="formmemo" label="추가 요청 및 건의사항" label-for="formmemo" description="요청사항을 작성해주세요.">
                <b-form-input id="formmemo" v-model="form.formmemo" type="text" required>
                </b-form-input>
            </b-form-group>

            <div class="btnwrap half">
                <b-button type="submit" variant="login">확인</b-button>
                <b-button type="reset" variant="cancel">취소</b-button>
            </div>
        </b-form>
    </Subpage>
</template>

<script>
import Subpage from "@/layout/components/Subpage.vue";
export default {
    components: { Subpage },
    data() {
        return {
            form: {
                reason: "",
                checkedtype: [],
                formname: "",
                formphone: "",
                formmemo: "",
            },
        };
    },
    methods: {
        Classcall(event) {
            event.preventDefault();
            alert("신청에 완료되었습니다.");
        },
    },
};
</script>