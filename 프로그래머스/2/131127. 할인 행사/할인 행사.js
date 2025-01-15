function solution(want, number, discount) {
    let temp = [];
    for(let i=0; i<want.length;i++){
        for(let ii=0; ii<number[i]; ii++){
            temp.push(want[i]);
        }
    }
    let result = 0;
    
    for (let i = 0; i <= discount.length - 10; i++) {
        let K = discount.slice(i, i + 10);

        // 조건 확인
        if (want.every((item, idx) => K.filter(x => x === item).length >= number[idx])) {
            result++;
        }
    }

    return result;
}