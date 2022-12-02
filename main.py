from itertools import count
from grab_dou import DouGrabber
from grab_upwork import UpworkGrabber
from stats.stats_counter import StatsCounter
from grab_djinni import DjinniGrabber
from stats.stats_merger import StatsMerger

if __name__ == '__main__':
    delimeter = "\n------------------------\n"
    # grabber = UpworkGrabber("seeding/seed-android-upwork.html", "results/results-upwork-android.txt", delimeter)
    # grabber.process()

    # grabber = DouGrabber('seeding/seed-flutter-dou.html', 'results/results-dou-flutter.txt', delimeter)
    # grabber.process()

    # grabber = DjinniGrabber(None, 'results/results-djinni-ios.txt', delimeter, "ios", number_of_pages=10)
    # texts = grabber.process()
    # grabber.write_results(texts)

    # counter = StatsCounter("results/results-djinni-ios.txt", 'stats/mobile-tech.csv', delimeter, "stats/stats-ios-djinni.txt")
    # counter.check()
    # counter.write_results()

    merger = StatsMerger(["stats/stats-flutter-djinni.txt", "stats/stats-flutter-dou.txt"], "stats/stats-flutter-total.txt")
    merger.process()
    merger.write_result()
