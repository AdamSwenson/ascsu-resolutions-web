<template>
    <div class="sponsor-select ">
        <label for="sponsor" class="form-label text-light">Sponsoring committee</label>
        <multiselect  v-model="value" :options="options" :searchable="false" :close-on-select="false"
                     :show-labels="false" placeholder="Select committeee"></multiselect>
        <pre class="language-json"><code>{{ value }}</code></pre>
    </div>

</template>

<script>
import Multiselect from 'vue-multiselect'

export default {
    name: "sponsor-select",
    components: {
        Multiselect
    },
    props: [],

    mixins: [],

    data: function () {
        return {
            value: '',
            options: ['Select option', 'options', 'selected', 'multiple', 'label', 'searchable', 'clearOnSelect', 'hideSelected', 'maxHeight', 'allowEmpty', 'showLabels', 'onChange', 'touched']

        }
    },

    asyncComputed: {},

    computed: {},

    methods: {}

}
</script>

<style scoped>

</style>
