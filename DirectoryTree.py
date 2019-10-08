# import os
# from flask import Flask, render_template
#
# """ """
# def make_tree(path):
#     tree = dict(name=os.path.basename(path), children=[])
#     print(tree)
#     try: lst = os.listdir(path)
#     except OSError:
#         pass  # ignore errors
#     else:
#         for name in lst:
#             if name.startswith('__'):
#                 pass
#             else:
#                 fn = os.path.join(path, name)
#                 if os.path.isdir(fn):
#                     tree['children'].append(make_tree(fn))
#                 else:
#                     tree['children'].append(dict(name=name))
#     return tree
#
#
# app = Flask(__name__)
#
#
# @app.route('/')
# def dirtree():
#     path = os.path.abspath('/home/ebryx/Desktop/test_runner/hello')
#     return render_template('dirtree.html', tree=make_tree(path))
#
#
# if __name__ == "__main__":
#     app.run(host='localhost', port=8888, debug=True)
