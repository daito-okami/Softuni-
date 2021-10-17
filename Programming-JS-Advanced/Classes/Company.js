class Company{
    constructor() {
        this.departments = {}

    }

    addEmployee(name, salary, position, department){
        if (!name|| !position|| !department || salary < 0){
            throw new Error("Invalid input!")
        }

        if (!this.departments[department]){
            this.departments[department] = []
        }
        this.departments[department].push({name, position, salary})
        return (`New employee is hired. Name: ${name}. Position ${position}`)
    }

    bestDepartment(){
        let currentBest = {
            name : "",
            salary: 0
        }
        for (let depKey in this.departments){
            let averageSalary = 0
            for (let empKey in this.departments[depKey]){
                averageSalary += this.departments[depKey][empKey]
            }
            averageSalary = averageSalary / this.departments[depKey].length
            if (currentBest.salary< averageSalary){
                currentBest.name = depKey
                currentBest.salary = averageSalary
            }
        }

        this.departments[currentBest.name].sort((a,b) =>{
            return b.salary - a.salary || a.name.localeCompare(b.name)
        })
        let bestDepartment = ""
        bestDepartment += `Best department is: ${currentBest.name}\n`
        bestDepartment += `Average salary: ${currentBest.salary.toFixed(2)}\n`
        this.departments[currentBest.name].forEach((el) =>{
            bestDepartment += `${el.name} ${el.salary} ${el.position}\n`
        })


        return bestDepartment
    }
}

let c = new Company();
c.addEmployee("Stanimir", 2000, "engineer", "Construction");
c.addEmployee("Pesho", 1500, "electrical engineer", "Construction");
c.addEmployee("Slavi", 500, "dyer", "Construction");
c.addEmployee("Stan", 2000, "architect", "Construction");
c.addEmployee("Stanimir", 1200, "digital marketing manager", "Marketing");
c.addEmployee("Pesho", 1000, "graphical designer", "Marketing");
c.addEmployee("Gosho", 1350, "HR", "Human resources");
console.log(c.bestDepartment());
