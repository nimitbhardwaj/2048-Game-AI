try:
    from main import main
except ImportError:
    from .main import main
import threading

if __name__ == '__main__':
    main()
