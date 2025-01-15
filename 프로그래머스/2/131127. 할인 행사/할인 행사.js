function solution(want, number, discount) {
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
