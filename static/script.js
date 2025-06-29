let currentStep = 0
const steps = document.querySelectorAll('.step')

function startWizard() {
    document.querySelector('.intro').style.display = 'none';
    document.querySelector('.container').style.display = 'block';
    // Optionally, show the first step if not already handled
    if (typeof showStep === 'function') showStep(0);
}

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
document.querySelector('.form').addEventListener('submit', function() {
    document.getElementById('loading-overlay').style.display = 'flex';
});