import sys

def f():
    wf = open('boos/xs_filter', 'w')
    product = set(ln.strip() for ln in open('标注过的/产品词', 'r'))
    brand = set(ln.strip() for ln in open('标注过的/品牌词', 'r'))
    for ln in open('boos/xs', 'r'):
        ln = ln.strip()
        if ln in product or ln in brand:
            continue
        wf.write('%s\n' % ln)
    print('finished')

def word_freq_dict():
    r = dict()
    for ln in open('/alidata1/songwt/title/fenci/word_freq', 'r'):
        ln = ln.strip()
        k, v = ln.split(',')
        r[k] = v
    return r

def dict_get(f, cixing):
    r = word_freq_dict() 
    wf = open('dict/%s_tag_dict' % f, 'w')
    wf2 = open('dict/%s_dict' % f, 'w')

    for ln in open('dict/%s' % f, 'r'):
        ln = ln.strip()
        freq = r.get(ln, 100)
        s = '%s%s%s%s%s%s' %(ln,'\3', cixing, '\2', freq, '\1')
        s2 = '%s%s%s' % (ln, '\1', freq)
        wf.write('%s\n' % s)
        wf2.write('%s\n' % s2)
    print('finished')


if __name__ == "__main__":
    #f()
    dict_get(sys.argv[1], sys.argv[2])
