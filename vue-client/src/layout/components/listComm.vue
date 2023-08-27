<template>
    <div class="listwrap">
        <div class="listnum">
            총 <strong v-html="lists.length"></strong>건이 등록되어 있습니다.
        </div>
        <div class="listbox">
            <div class="listitem" v-for="(item, index) in lists" :key="index">
                <div class="listthum"><img :src="item.img" /></div>
                <div class="listdetail">
                    <strong v-html="item.title"></strong>
                    <div class="listdate">등록일 : {{ item.date }}</div>
                    <div class="listdec" v-html="item.dec"></div>
                    <div class="itembtns">
                        <b-button variant="listdown" :href="item.link">
                            <i class="bi bi-youtube" />영상 보러 가기
                        </b-button>
                    </div>
                    <div class="downguide">
                        ⌘ 영상보기가 안될 경우 <br />
                        인터넷 연결 문제 등으로 영상으로 넘어가지 않을 수 있습니다. <br />
                        인터넷 연결 문제가 아니라면, 고객센터로 연락주시면 감사하겠습니다.
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    props: ["lists"],
};
</script>