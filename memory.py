import json
import os


class Memory:

    def __init__(self, filename="experiences.json"):

        self.filename = filename

        if os.path.exists(self.filename):

            try:

                with open(
                    self.filename,
                    "r",
                    encoding="utf-8"
                ) as file:

                    self.experiences = json.load(file)

            except (json.JSONDecodeError, OSError):

                self.experiences = []

        else:

            self.experiences = []

    # ---------------------------------
    # SAVE EXPERIENCE
    # ---------------------------------

    def remember(self, experience):

        self.experiences.append(experience)

        self._save()

    # ---------------------------------
    # SAVE TO FILE
    # ---------------------------------

    def _save(self):

        with open(
            self.filename,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                self.experiences,
                file,
                indent=4,
                ensure_ascii=False
            )

    # ---------------------------------
    # GET ALL MEMORIES
    # ---------------------------------

    def get_memories(self):

        return self.experiences

    # ---------------------------------
    # GET RELEVANT MEMORIES
    # ---------------------------------

    def get_relevant_memories(self, task, limit=5):

        task_words = set(
            task.lower().split()
        )

        scored_memories = []

        for memory in self.experiences:

            memory_text = (
                memory.get("task", "") + " " +
                memory.get("lesson", "")
            ).lower()

            memory_words = set(
                memory_text.split()
            )

            score = len(
                task_words.intersection(
                    memory_words
                )
            )

            if score > 0:

                scored_memories.append(
                    (score, memory)
                )

        scored_memories.sort(
            key=lambda item: item[0],
            reverse=True
        )

        return [
            memory
            for score, memory
            in scored_memories[:limit]
        ]