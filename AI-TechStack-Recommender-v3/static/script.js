let selectedSkills = [];
let matchChartInstance = null;
let coverageChartInstance = null;
let globalResults = null;

const allSkillsData = {
    "Programming": ["Python", "Java", "JavaScript", "TypeScript", "C++", "Go"],
    "Frontend": ["React", "HTML", "CSS", "Vue", "Angular"],
    "Backend": ["Node.js", "Django", "Flask", "Spring", "Express"],
    "Data Science": ["SQL", "Pandas", "Power BI", "Excel", "Statistics"],
    "AI/ML": ["TensorFlow", "PyTorch", "Machine Learning", "Deep Learning", "Scikit-Learn"],
    "Cloud": ["AWS", "Azure", "GCP", "Terraform"],
    "DevOps": ["Docker", "Kubernetes", "CI/CD", "Linux", "Git"]
};

function populateCategories() {
    const container = document.getElementById('categories');
    container.innerHTML = '';
    Object.keys(allSkillsData).forEach(cat => {
        const div = document.createElement('div');
        div.className = 'p-3 mb-1 rounded-3 category-item';
        div.textContent = cat;
        container.appendChild(div);
    });
}

function populateSkills(filter = '') {
    const container = document.getElementById('all-skills');
    container.innerHTML = '';
    Object.values(allSkillsData).flat().forEach(skill => {
        if (!skill.toLowerCase().includes(filter.toLowerCase())) return;
        const chip = document.createElement('div');
        chip.className = `skill-chip ${selectedSkills.includes(skill) ? 'selected' : ''}`;
        chip.textContent = skill;
        chip.onclick = () => toggleSkill(skill, chip);
        container.appendChild(chip);
    });
}

function toggleSkill(skill, el) {
    if (selectedSkills.includes(skill)) {
        selectedSkills = selectedSkills.filter(s => s !== skill);
        el.classList.remove('selected');
    } else {
        selectedSkills.push(skill);
        el.classList.add('selected');
    }
    updateSelected();
}

function updateSelected() {
    const container = document.getElementById('selected-skills');
    container.innerHTML = '';
    selectedSkills.forEach(skill => {
        const chip = document.createElement('div');
        chip.className = 'skill-chip selected d-inline-flex align-items-center gap-2 px-4 py-2 me-2 mb-2';
        chip.innerHTML = `${skill} <span onclick="removeSkill('${skill}');event.stopImmediatePropagation()" style="cursor:pointer">×</span>`;
        container.appendChild(chip);
    });
    document.getElementById('hidden-skills').value = selectedSkills.join(',');
    document.getElementById('count').textContent = selectedSkills.length;
}

function removeSkill(skill) {
    selectedSkills = selectedSkills.filter(s => s !== skill);
    updateSelected();
    populateSkills(document.getElementById('skill-search').value);
}

function filterSkills() {
    populateSkills(document.getElementById('skill-search').value);
}

function animateProgressBars() {
    document.querySelectorAll('.progress-bar-animated').forEach(bar => {
        const targetWidth = bar.style.width;
        bar.style.width = '0%';
        setTimeout(() => bar.style.width = targetWidth, 150);
    });
}

function initCharts(results = null) {
    const effectiveResults = results || globalResults;
    const isLight = document.body.getAttribute('data-theme') === 'light';
    
    const matchCtx = document.getElementById('matchChart');
    if (matchChartInstance) matchChartInstance.destroy();
    
    const labels = effectiveResults ? effectiveResults.slice(0, 6).map(r => r.role) : ["AI Engineer", "Data Scientist", "Full Stack", "Backend", "DevOps", "Cloud Engineer"];
    const scores = effectiveResults ? effectiveResults.slice(0, 6).map(r => r.score) : [92, 85, 78, 65, 71, 59];
    
    matchChartInstance = new Chart(matchCtx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: 'Match %',
                data: scores,
                backgroundColor: isLight ? 'rgba(124, 58, 237, 0.85)' : 'rgba(99, 102, 241, 0.85)',
                borderColor: isLight ? '#7c3aed' : '#6366f1',
                borderWidth: 1,
                borderRadius: 8,
                barThickness: 32
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: { legend: { display: false } },
            scales: {
                y: { 
                    max: 100, 
                    grid: { color: isLight ? 'rgba(0,0,0,0.08)' : 'rgba(255,255,255,0.1)' },
                    ticks: { color: isLight ? '#475569' : '#e0e0ff' }
                },
                x: { 
                    grid: { color: isLight ? 'rgba(0,0,0,0.08)' : 'rgba(255,255,255,0.1)' },
                    ticks: { color: isLight ? '#475569' : '#e0e0ff' }
                }
            }
        }
    });

    const coverCtx = document.getElementById('coverageChart');
    if (coverageChartInstance) coverageChartInstance.destroy();
    const topScore = effectiveResults && effectiveResults.length > 0 ? effectiveResults[0].score : 75;
    
    coverageChartInstance = new Chart(coverCtx, {
        type: 'doughnut',
        data: {
            labels: ['Matched', 'To Learn'],
            datasets: [{
                data: [topScore, 100 - topScore],
                backgroundColor: ['#22c55e', '#eab308'],
                borderWidth: 0,
                cutout: '78%'
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: { 
                    position: 'bottom', 
                    labels: { 
                        color: isLight ? '#1e2937' : '#f1f5f9',
                        padding: 20,
                        font: { size: 14 }
                    } 
                }
            }
        }
    });
}

function resetApp() {
    // 👈 إزالة selectedSkills من localStorage قبل الreload
    localStorage.removeItem('selectedSkills');
    window.location.href = '/';  // 👈 يعود للصفحة الرئيسية (Flask)
}

document.getElementById('recommend-form').addEventListener('submit', function(e) {
    if (selectedSkills.length === 0) {
        e.preventDefault();
        alert("Please select at least one skill!");
        return;
    }
    const btn = document.getElementById('submit-btn');
    btn.innerHTML = `<span class="spinner-border spinner-border-sm me-3"></span> AI is analyzing...`;
    btn.disabled = true;
    // 👈 الـ form سيسubmit طبيعياً لـ Flask (POST) - الـ result يظهر بعد الرد
});

window.addEventListener('load', () => {
    populateCategories();
    populateSkills();
    
    const savedTheme = localStorage.getItem('theme') || 'dark';
    document.body.setAttribute('data-theme', savedTheme);
    
    const icon = document.querySelector('.theme-toggle i');
    if (savedTheme === 'light' && icon) icon.classList.replace('fa-moon', 'fa-sun');
    
    // 👈 قراءة globalResults من الـ script#results-json
    const resultsScript = document.getElementById('results-json');
    if (resultsScript && resultsScript.textContent.trim()) {
        globalResults = JSON.parse(resultsScript.textContent);
    }
    
    if (!document.getElementById('results-section').classList.contains('d-none')) {
        setTimeout(() => {
            animateProgressBars();
            initCharts(globalResults);
        }, 300);
    }
});

function toggleTheme() {
    const body = document.body;
    const newTheme = body.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
    body.setAttribute('data-theme', newTheme);
    localStorage.setItem('theme', newTheme);
    
    const icon = document.querySelector('.theme-toggle i');
    if (icon) {
        icon.classList.toggle('fa-moon', newTheme === 'dark');
        icon.classList.toggle('fa-sun', newTheme === 'light');
    }
    
    if (!document.getElementById('results-section').classList.contains('d-none')) {
        setTimeout(() => {
            initCharts(globalResults);
        }, 100);
    }
}