import numpy as np

floats = np.random.random_sample((5,))*20

def histogram (lst):
    print('  '+chr(195))
    for i in range(len(lst)):
        print(i, chr(179)+chr(178-i%2) * int(lst[i]), end='')
        print(' {:.2f} '.format(lst[i]), end=' ')
        print('<== MAX'*int(lst[i] == max(lst)), '<== MIN'*int(lst[i] == min(lst)))
        print('  '+chr(195))
    print('\nSummary\n'+'='*20)
    print('{:<10}{:>10.2f}'.format('Mean:', np.mean(lst)))
    print('{:<10}{:>10.2f}'.format('Median:', np.median(lst)))
    print('{:<10}{:>10.2f}'.format('Max:', max(lst)))
    print('{:<10}{:>10.2f}'.format('Min:', min(lst)))
    print('{:<10}{:>10.2f}'.format('St_Dev:', np.std(lst)))

histogram(floats)

#END