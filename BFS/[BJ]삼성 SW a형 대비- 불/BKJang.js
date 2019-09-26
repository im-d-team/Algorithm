class Queue {
  constructor() {
    this.arr = [];
  }
  enQueue(item) {
    this.arr.push(item);
  }
  deQueue() {
    return this.arr.shift();
  }
}

let input = [];

require('readline')
  .createInterface(process.stdin, process.stdout)
  .on('line', function (line) {
    input.push(line.trim())
  })
  .on('close', function () {
    const numberOfTestCase = input.shift();
    //1. testCase만큼 반복
    for (let i = 0; i < numberOfTestCase; i++) {
      //2. 각각의 테스트 케이스를 2차원 배열로 바꾼다.
      const testCase = input.shift().split(' ');
      const w = testCase[0];
      const h = testCase[1];
      const inputArr = [];

      for (let j = 0; j < h; j++) {
        const testCaseLine = input.shift();
        inputArr[j] = testCaseLine.split('');
      }
      const answer = dfs({ inputArr, w, h });
      console.log(answer);
    }
  });

const dfs = ({ inputArr, w, h }) => {
  const queue = new Queue();

  // 3. inputArr를 각 값에 따라 바꿔준다.
  handleChangeInputArr({ inputArr, w, h, queue });
  // 4. 큐가 비워질 때까지 반복한다.
  let isFire = false;
  let isPossible = false;
  let result = 0;

  while (queue.arr.length > 0) {
    const item = queue.deQueue();
    if (item.fire) {
      isFire = true;
    } else {

      if (isFire && !item.fire)
        result++;
      isFire = false;
    }

    const possible = handleMoveFireAndPerson({ inputArr, item, queue });

    if (possible) {
      isPossible = true;
    }
  }

  if (isPossible) return result;

  return 'IMPOSSIBLE'
}

const handleChangeInputArr = ({ inputArr, w, h, queue }) => {
  for (let i = 0; i < h; i++) {
    for (let j = 0; j < w; j++) {
      switch (inputArr[i][j]) {
        case '.':
          inputArr[i][j] = 0;
          break;
        case '#':
          inputArr[i][j] = 2;
          break;
        case '*':
          inputArr[i][j] = -1;
          queue.enQueue({ x: i, y: j, fire: true })
          break;
        case '@':
          inputArr[i][j] = 0;
          queue.enQueue({ x: i, y: j });
          break;
        default:
          throw new Error('unsupported type');
      }
    }
  }
}

const handleMoveFireAndPerson = ({ inputArr, item, queue }) => {
  const degrees = [{ x: 0, y: 1 }, { x: 0, y: -1 }, { x: 1, y: 0 }, { x: -1, y: 0 }];
  let possible = false;

  if ((item.x === 0 || item.y === 0 || item.x === inputArr.length - 1 || item.y === inputArr[0].length - 1) && !item.fire) {
    possible = true;
  }

  degrees.forEach(degree => {
    const locationArr = inputArr[item.x + degree.x];
    const location = locationArr && locationArr[item.y + degree.y]

    if (location === 0) {
      if (item.fire) {
        inputArr[item.x + degree.x][item.y + degree.y] = -1;
        queue.enQueue({ x: item.x + degree.x, y: item.y + degree.y, fire: true });
      } else {
        inputArr[item.x + degree.x][item.y + degree.y] = 0;
        queue.enQueue({ x: item.x + degree.x, y: item.y + degree.y });
      }
    }
  });
  
  return possible;
}
