def main():
    def task(name, work_queue):
        if work_queue.empty():
            print(f"Task {name} nothing to do")
        else:
            while not work_queue.empty():
                count = work_queue.get()
                total = 0
                print(f"Task {name} running")
                for _ in range(count):
                    total += 1
                    yield
                print(f"Task {name} total: {total}")

    import queue

    work_queue = queue.Queue()

    for work in [15, 10, 5, 2]:
        work_queue.put(work)

    # version1
    # tasks = [(task, "One", work_queue), (task, "Two", work_queue)]
    # for task, name, queue in tasks:
    #     task(name, queue)
    # Task One running
    # Task One total: 15
    # Task One running
    # Task One total: 10
    # Task One running
    # Task One total: 5
    # Task One running
    # Task One total: 2
    # Task Two nothing to do

    # version2
    # tasks = [task("One", work_queue), task("Two", work_queue)]
    # done = False
    # while not done:
    #     for task in tasks:
    #         try:
    #             next(task)
    #         except StopIteration:
    #             tasks.remove(task)
    #         if len(tasks) == 0:
    #             done = True
    # Task One running
    # Task Two running
    # Task Two total: 10
    # Task Two running
    # Task One total: 15
    # Task One running
    # Task Two total: 5
    # Task One total: 2


main()
