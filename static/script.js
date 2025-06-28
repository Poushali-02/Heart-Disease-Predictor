let currentStep = 0
const steps = document.querySelectorAll('.step')

function showStep(index){
    steps.forEach((step, i) => {
        if (i === index){
            step.classList.add('active')
        }
        else{
            step.classList.remove('active')
        }
    })
}

function nextStep(){
    if (currentStep < steps.length - 1)
        currentStep++
    showStep(currentStep)
}

function prevStep(){
    if (currentStep > 0)
        currentStep--
    showStep(currentStep)
}

document.addEventListener('DOMContentLoaded', () => showStep(currentStep));