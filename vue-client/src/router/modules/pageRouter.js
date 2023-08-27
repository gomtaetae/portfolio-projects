const withPrefix = (prefix, routes) =>
    routes.map((route) => {
        route.path = prefix + route.path;
        return route;
    });


const pageRouter = {
    path : "/",
    name : "layout",
    redirect : "/main",     // 처음 접속할 때 바로 main.vue 컴포넌트가 바로 출력된다
    component : () => import("@/layout/index.vue"),
    children : [
        {
            path : "/main",
            name : "main",
            component : () => import("@/views/main.vue"),
        },
        {
            path: "/video",
            name: "video",
            component: () => import("@/views/video.vue"),
        },
        {
            path: "/counsil",
            name: "counsil",
            component: () => import("@/views/classsample.vue"),
        },
        {
            path: "/intro",
            name: "intro",
            component: () => import("@/views/intro.vue")
        },
        ...withPrefix("/medicine", [
            {
                path: "/",
                component: () => import("@/views/Medicine.vue"),
            },
            {
                name: "medicine",
                path: "/:tabID",
                component: () => import("@/views/Medicine.vue"),
            },
        ]), 
        {
            path : "/mypage",
            name : "mypage",
            component : () => import("@/views/MyPage.vue"),
        },        
        {
            path : "/medcom",
            name : "medcom",
            component : () => import("@/views/MedCompany.vue"),
        },      
        {
            path : "/road",
            name : "road",
            component : () => import("@/views/RoadView.vue"),
        },
        {
            path : "/userdata",
            name : "userdata",
            component : () => import("@/views/userdata.vue"),
        },
        {
            path : "/productInfo",
            name : "productInfo",
            component : () => import("@/views/productInfo.vue"),
        },
    ],
};

export default pageRouter;