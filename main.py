
from views.main_view import  MainView


def main():
  v = MainView.load_view()
  v.present(style='fullscreen', orientations=['portrait'])
  
  
if __name__ == '__main__':
  main()
