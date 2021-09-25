function ex(obj){
    if (obj.dizziness){
        obj.leveOfHydrated += obj.weight * obj.experience * 0.1;
        obj.dizziness  = false;
    }

    return obj
}