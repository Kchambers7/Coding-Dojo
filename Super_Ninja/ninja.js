class Ninja {
    constructor(name, health, strength = 3, speed = 3) {
        this.name = name;
        this.health = health;
        this.speed = speed;
        this.strength = strength;
    }
    sayName() {
        console.log(this.name);
        return this;
    }
    showStats() {
        console.log(this.name, this.health, this.speed, this.strength);
        return this;
    }
    drinkSake() {
        this.health += 10;
        console.log('You drank sake and increased your health by 10')
        console.log(this.health);
        return this;
    }
}

class Sensei extends Ninja {
    constructor(name, health=200, speed=10, strength=10, wisdom=10) {
        super(name);
        this.health = health;
        this.speed = speed;
        this.strength = strength;
        this.wisdom = wisdom;
    }
    speakWisdom() {
        const dranksake = super.drinkSake();
        console.log("The reason women dont play football is because 11 of them would never wear the same outfit in public");
        return this;
    }
    showStats() {
        console.log(this.name, this.health, this.speed, this.strength, this.wisdom);
        return this;
    }
}

const sensei1 = new Sensei("Katelyn");
sensei1.speakWisdom();
sensei1.showStats();