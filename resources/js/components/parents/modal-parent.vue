<template>

    <!-- Modal -->
    <div class="modal fade"
         v-bind:id="modalId"
         tabindex="-1"
         v-bind:aria-labelledby="labelId"
         aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">

                <div class="modal-header">
                    <h5 class="modal-title"
                        v-bind:id="labelId"
                    >{{ modalTitle }}</h5>

                    <button
                        type="button"
                        class="btn-close"
                        data-bs-dismiss="modal"
                        aria-label="Close"
                        v-on:click="handleCancel"
                    ></button>

                </div>

                <div class="modal-body">
                    <div class="modalText" v-html="modalText"></div>
                    <slot>
                        <div class="modalText" v-html="modalSecondaryText"></div>
                    </slot>
                </div>

                <div class="modal-footer">
                    <button type="button"
                            class="btn btn-secondary"
                            data-bs-dismiss="modal"
                            v-on:click="handleCancel"
                    >Cancel
                    </button>


                    <button type="button"
                            class="btn btn-primary"
                            v-if="showActionButton"
                            data-bs-dismiss="modal"
                            v-on:click="handleClick"
                    >{{ buttonLabel }}
                    </button>

                </div>
            </div>
        </div>
    </div>

</template>

<script>

import {isReadyToRock} from "../../utilities/readiness.utilities";

/**
 * Note, this will require that a corresponding button which inherits from
 * modal-button-parent is included elsewhere on the page
 * They are linked via  bootstrap
 * using the data-bs-dismiss=modal attribute.
 *
 * Content of the modal is either defined via the slot
 *      <modal-child>
 *          stuff that goes in modal
 *       </modal-child>
 * or by defining modalSecondaryText in data or property
 *
 * Children must define (data or property):
 *      modalId
 *      modalTitle
 *      handleClick
 *      buttonLabel : The label on the action button
 *
 * Children may define (data or property):
 *      styling
 *      modalText
 *      hideActionButton : Boolean of whether to hide the action button.
 *                          mostly used when a button will be used in the slot
 *
 * handleCancel
 */
export default {
    name: "modal-parent",

    props: [],

    mixins: [],

    computed: {
        showActionButton: function () {
            if (!isReadyToRock(this.hideActionButton)) return true;
            return !this.hideActionButton;
        },

        labelId: function () {
            return "modalLabelId" + this.modalId;
        },

    },

    methods: {
        closeModal: function () {
            // $('#' + this.modalId).modal('hide');
            var myModalEl = document.getElementById(this.modalId);
            var modal = bootstrap.Modal.getInstance(myModalEl)
            modal.hide();
        },

        handleCancel : function(){}

    }

}

</script>

<style scoped>

</style>
