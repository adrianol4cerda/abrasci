function calculatePoints() {
    let points = 0;
    
    // Idade
    const age = parseInt(document.getElementById('idade').value);
    if (age >= 80) {
        points += 1;
    }
    
    // Suporte social
    const support = document.querySelector('input[name="suporte-social"]:checked');
    if (support && support.value === 'Sim') {
        points += 1;
    }

	// Condições crônicas
    const chronicConditions = document.querySelectorAll('input[name="condicoes-cronicas"]:checked');
    if (chronicConditions.length === 0) {
        points += 1;
    } else if (chronicConditions.length <= 2) {
        points += 1;
    } else {
        points += 2;
    }

    
    // Medicamentos
    const medications = parseInt(document.getElementById('medicamentos').value);
    if (medications >= 5) {
        points += 1;
    }
    
    // Internações
    const hospitalizations = parseInt(document.getElementById('internacoes').value);
    if (hospitalizations >= 2) {
        points += 1;
    }

    // Quedas
    const falls = document.querySelector('input[name="quedas"]:checked');
   	if (falls && falls.value === 'Sim') {
        points += 1;
    }
    
    // Visão
    const vision = document.querySelector('input[name="visao"]:checked');
    if (vision && vision.value === 'Sim') {
        points += 1;
    }
    
    // Audição
    const hearing = document.querySelector('input[name="audiçao"]:checked');
    if (hearing && hearing.value === 'Sim') {
        points += 1;
    }
    
    // Limitação física
    const physicalLimitation = document.querySelector('input[name="limitacao-fisica"]:checked');
    if (physicalLimitation && physicalLimitation.value === 'Sim') {
        points += 1;
    }
    
    // Cognição
    const cognition = document.querySelector('input[name="cognicao"]:checked');
    if (cognition && cognition.value === 'Sim') {
        points += 1;
    }
    
    // Humor
    const mood = document.querySelector('input[name="humor"]:checked');
    if (mood && mood.value === 'Sim') {
        points += 1;
    }
    
    // Atividades básicas de vida diária
    const dailyActivities = document.querySelector('input[name="atividades-basicas"]:checked');
    if (dailyActivities && dailyActivities.value === 'Sim') {
        points += 1;
    }
    
    // Atividades instrumentais de vida diária
    const instrumentalActivities = document.querySelector('input[name="atividades-instrumentais"]:checked');
    if (instrumentalActivities && instrumentalActivities.value === 'Sim') {
        points += 1;
    }
    
    // Incontinência
    const incontinence = document.querySelector('input[name="incontinencia"]:checked');
    if (incontinence && incontinence.value === 'Sim') {
        points += 1;
    }
    
    // Perda de peso não intencional
    const weightLoss = document.querySelector('input[name="perda-peso"]:checked');
    if (weightLoss && weightLoss.value === 'Sim') {
        points += 1;
    }
    
    // Abandono
    const abandonment = document.querySelector('input[name="abandono"]:checked');
    if (abandonment && abandonment.value === 'Sim') {
        points += 1;
    }
    
    return points;
}

