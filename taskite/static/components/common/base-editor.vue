<script setup>
import { ref } from 'vue'

// import ClassicEditor from '@ckeditor/ckeditor5-build-classic'
import { ClassicEditor } from '@ckeditor/ckeditor5-editor-classic'

import { Essentials } from '@ckeditor/ckeditor5-essentials'
import { Bold, Italic } from '@ckeditor/ckeditor5-basic-styles'
import { Link } from '@ckeditor/ckeditor5-link'
import { Paragraph } from '@ckeditor/ckeditor5-paragraph'
import CKEditor from '@ckeditor/ckeditor5-vue'

const props = defineProps(['modelValue'])
const emit = defineEmits(['update:modelValue'])

const editor = ref(ClassicEditor)
const editorConfig = {
  plugins: [Essentials, Bold, Italic, Link, Paragraph],
  toolbar: {
    items: ['bold', 'italic', 'link', 'undo', 'redo'],
  },
}
const ckeditor = CKEditor.component

const handleInput = (value) => {
  emit('update:modelValue', value)
}
</script>

<template>
  <ckeditor
    :editor="editor"
    :config="editorConfig"
    :modelValue="props.modelValue"
    @input="handleInput"
  ></ckeditor>
</template>

<style>
.ck-editor__editable_inline {
  height: 380px;
  overflow-y: auto;
}
</style>
