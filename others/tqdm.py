from tqdm import tqdm

if __name__ == '__main__':
    number = range(int(10e7))
    for i in tqdm(number, colour = 'green', desc='in Processing'):
        pass
