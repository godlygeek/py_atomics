import os
import string

import setuptools

this_dir = os.path.dirname(__file__)
exec(open(os.path.join(this_dir, "generator.py")).read())

with open(os.path.join(this_dir, 'py_atomics.pyx'), 'w') as pyx:
    pyx.write(HEADER)
    template = string.Template(PER_INT_TYPE)
    pyx.write(template.substitute(INT_TYPE='uint8_t'))
    pyx.write(template.substitute(INT_TYPE='uint16_t'))
    pyx.write(template.substitute(INT_TYPE='uint32_t'))
    pyx.write(template.substitute(INT_TYPE='uint64_t'))
    pyx.write(template.substitute(INT_TYPE='int8_t'))
    pyx.write(template.substitute(INT_TYPE='int16_t'))
    pyx.write(template.substitute(INT_TYPE='int32_t'))
    pyx.write(template.substitute(INT_TYPE='int64_t'))
    pyx.write(FOOTER)
    
module1 = setuptools.Extension(
    'py_atomics',
    sources=['py_atomics.pyx'],
    extra_compile_args=['-std=c11'],
)

setuptools.setup(
    name='py_atomics',
    version = '0.1',
    description='Python atomics',
    author='doodspav',
    ext_modules=[module1],
)
