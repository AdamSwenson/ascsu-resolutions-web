<template>
    <footer class="bd-footer py-5 mt-5 ">
        <div class="container py-5">
            <div class="row">
                <div class="col-lg-3 mb-3">

                    <ul class="list-unstyled small text-light">
<!--                    <ul class="list-unstyled small text-muted">-->
                        <li class="mb-2">Designed and built by Adam Swenson</li>
                        <li class="mb-2">{{appVersion}}</li>
                    </ul>

                </div>

                <div class="col-6 col-lg-2 offset-lg-1 mb-3">

                </div>
                <div class="col-6 col-lg-2 mb-3">

                </div>
                <div class="col-6 col-lg-2 mb-3">

                    <ul class="list-unstyled helpLinks">
                        <li class="mb-2 text-light text-bold"><span class="text-light"><a href="https://github.com/AdamSwenson/ascsu-resolutions-web#readme"  target="_blank" rel="noopener noreferrer">FAQs and instructions</a></span></li>
                        <li class="mb-2 text-light"><a href="https://github.com/AdamSwenson/ascsu-resolutions-web/issues"  target="_blank" rel="noopener noreferrer">Feedback</a></li>
                     </ul>
                </div>
                <div class="col-6 col-lg-2 mb-3">

                </div>
            </div>

            <div class="page-spacer"></div>
        </div>
    </footer>
</template>

<script>
import {isReadyToRock} from "../../utilities/readiness.utilities";

export default {
    name: "page-footer",

    props: [],

    mixins: [],

    data: function () {
        return {}
    },

    asyncComputed: {
        appVersion: function(){
            if(isReadyToRock(window.appVersion)) return 'Currently v.' + window.appVersion ;
            return ''
        }
    },

    computed: {},

    methods: {}

}
</script>

<style scoped>
.helpLinks{
    color: white;
}
</style>
