class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
                # This builds the unique values so I can check membership quickly.  # change this: the naive version scanned nums each time.
        # I need it to reach O(n) average time, and set(nums) builds it in O(n) average time.  # change this: this replaces repeated full scans.
        # It handles empty input and duplicates, but the tradeoff is O(n) extra space.  # change this: the naive version used O(1) extra space.
        values = set(nums)  # change this: add a set so each lookup is O(1) average instead of O(n).

        # This stores the longest length found, and zero makes the empty case work.  # change this: best is now updated only from real starts.
        # Updating it costs O(1), uses O(1) space, and avoids a separate empty-input branch.  # change this: the update flow is different.
        # The tradeoff is only that I keep one extra integer, which is constant space.  # change this: explain the optimized tracking.
        best = 0

        # This visits each unique number because duplicates cannot extend a sequence.  # change this: loop over the set instead of nums.
        # I need unique values to avoid repeated work, and the whole loop is O(n) average overall.  # change this: remove duplicate starts.
        # It handles all-duplicate input, but set iteration does not follow input order, which does not matter here.  # change this: order is no longer used.
        for num in values:  # change this: process unique values instead of every array entry.

            # This checks whether num is the true beginning of its sequence.  # change this: add the sequence-start check.
            # I need it so middle values do not rebuild the same sequence, and the lookup is O(1) average.  # change this: avoid repeated counting.
            # It handles negative and large values, with the tradeoff that hash performance is average-case.  # change this: use set membership.
            if num - 1 not in values:  # change this: only count when the previous consecutive value is absent.

                # This starts the sequence length at one because num itself is present.  # change this: initialize only for a real start.
                # I need it for isolated values, and it uses O(1) time and space.  # change this: no sequence is built for middle values.
                # The tradeoff is that I store only the length, so I do not return the sequence itself.  # change this: track only the requested result.
                length = 1  # change this: count a sequence only after confirming its start.

                # This stores the next value I want to find so each step moves forward by exactly one.  # change this: replace current plus repeated scans.
                # I need it to follow the consecutive rule, and initialization costs O(1).  # change this: set up direct set lookups.
                # It works at integer boundaries used by the problem, with only one extra integer of space.  # change this: no array indexing is used.
                next_num = num + 1  # change this: directly prepare the next consecutive value.

                # This extends the sequence while the next value exists in the set.  # change this: replace the full-array search loop.
                # I need it to count the sequence, and each lookup is O(1) average.  # change this: membership is now direct.
                # Across all starts it visits each sequence value once, but it uses the extra set memory.  # change this: total work becomes O(n) average.
                while next_num in values:  # change this: use set membership instead of scanning every input value.

                    # This counts the value I just found, using O(1) time and space per step.  # change this: extend after a direct lookup.
                    # I need it for the final length, and it handles long sequences without storing them.  # change this: keep only a counter.
                    # The tradeoff is that I cannot return the members without doing more work.  # change this: optimize for the requested length.
                    length += 1  # change this: increment after confirming the next value in the set.

                    # This advances to the next required value, which keeps the sequence exactly consecutive.  # change this: move a lookup key instead of rescanning.
                    # I need it to stop at the first gap, and each update costs O(1).  # change this: the loop follows direct integer keys.
                    # It handles negative values normally, with no meaningful extra-space cost.  # change this: support every allowed integer directly.
                    next_num += 1  # change this: check the next integer through the set on the next loop.

                # This keeps the largest completed sequence after the first missing value.  # change this: update only after counting from a valid start.
                # I need it for the answer, and max costs O(1) time with O(1) space.  # change this: replace the naive conditional update.
                # It handles isolated values because their length stays one, with no extra data structure.  # change this: use one direct update.
                best = max(best, length)  # change this: compare only fully counted, non-repeated sequences.

        # This returns zero for empty input and the largest sequence length otherwise.
        # It costs O(1), needs no extra work, and does not change the input.
        # The tradeoff is that it returns only the length, exactly as the problem asks.
        return best