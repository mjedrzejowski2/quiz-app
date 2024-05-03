<script setup>
import { ref, computed } from "vue";

const questions = ref([
  {
    question: 'Which of the following is not a data type in JavaScript?',
    answer: 3,
    options: [
      'String',
      'Number',
      'Boolean',
      'Character'
    ],
    selected: null
  },
  {
    question: 'What is the purpose of the box-sizing property in CSS?',
    answer: 1,
    options: [
      'To control the visibility of an element',
      'To include padding and border in the width and height of an element',
      'To set the background color of an element',
      'To adjust the font size of text within an element'
    ],
    selected: null
  },
  {
    question: 'Which HTML element is used to create a link?',
    answer: 2,
    options: [
      '<button>',
      '<img>',
      '<a>',
      '<div>'
    ],
    selected: null
  }
])

const quizCompleted = ref(false)
const currentQuestion = ref(0)
const score = computed(() => {
  let value = 0
  questions.value.map(q => {
    if (q.selected == q.answer) {
      value++
    }
  })
  return value
})
</script>

<template>
  <h1>Hello world</h1>
  <p>Witoj</p>
</template>

<style>
* { 
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: 'Montserrat', sans-serif;
}

body {
  background-color: #271c36;
  color: #FFF;
}
</style>