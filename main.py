from itertools import count
from grab_dou import DouGrabber
from grab_upwork import UpworkGrabber
from stats.stats_counter import StatsCounter
from grab_djinni import DjinniGrabber

if __name__ == '__main__':
    delimeter = "\n------------------------\n"
    # grabber = UpworkGrabber("seeding/seed-android-upwork.html", "results/results-upwork-android.txt", delimeter)
    # grabber.process()

    grabber = DouGrabber('seeding/seed-android-dou.html', 'results/results-dou-android.txt', delimeter)
    grabber.process()

    # grabber = DjinniGrabber(None, 'results/results-djinni-flutter.txt', delimeter, "flutter", number_of_pages=4)
    # texts = grabber.process()
    # grabber.write_results(texts)

    counter = StatsCounter("results/results-dou-android.txt", 'stats/mobile-tech.csv', delimeter, "stats/stats-android-dou.txt")
    counter.check()
    counter.write_results()
