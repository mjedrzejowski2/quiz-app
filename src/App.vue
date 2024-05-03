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
const getCurrentQuestion = computed(() => {
    let question = questions.value[currentQuestion.value]
    question.index = currentQuestion.value
    return question
})

const setAnswer = evt => {
    questions.value[currentQuestion.value].selected = evt.target.value
    evt.target.value = null
}

const NextQuestion = () => {
    if (currentQuestion.value < question.value.length - 1) {
        currentQuestion.value++
    } else {
        quizCompleted.value = true
    }
}
</script>

<template>
    <main class="app">
        <h1>The quiz</h1>

        <section class="quiz"></section>
            <div class="quiz-info">
                <span class="question">{{ getCurrentQuestion.question }}</span>
                <span class="score"> Score {{ score }} / {{ questions.length }}</span>
            </div>
            

    </main>

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