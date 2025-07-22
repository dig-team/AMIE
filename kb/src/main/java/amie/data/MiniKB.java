package amie.data;

import it.unimi.dsi.fastutil.ints.Int2IntMap;
import it.unimi.dsi.fastutil.ints.Int2IntOpenHashMap;

import static amie.data.U.increase;

public class MiniKB extends KB {

    /**
     * Adds a fact to the KB
     *
     * @param subject
     * @param relation
     * @param object
     * @return TRUE if the KB was changed, i.e., the fact did not exist before.
     */
    @Override
    protected boolean add(int subject, int relation, int object) {
        if (!add(subject, relation, object, subject2relation2object))
            return (false);
        if (!add(relation, object, subject, relation2object2subject))
            return false;
        //add(object, subject, relation, object2subject2relation);
        add(relation, subject, object, relation2subject2object);
/*      add(object, relation, subject, object2relation2subject);
        add(subject, object, relation, subject2object2relation);*/
        synchronized (subjectSize) {
            increase(subjectSize, subject);
        }
        synchronized (relationSize) {
            increase(relationSize, relation);
        }
        synchronized (objectSize) {
            increase(objectSize, object);
        }

        synchronized (subject2subjectOverlap) {
            Int2IntMap overlaps = subject2subjectOverlap
                    .get(relation);
            if (overlaps == null) {
                subject2subjectOverlap.put(relation,
                        new Int2IntOpenHashMap());
            }
        }

        synchronized (subject2objectOverlap) {
            Int2IntMap overlaps = subject2objectOverlap
                    .get(relation);
            if (overlaps == null) {
                subject2objectOverlap.put(relation,
                        new Int2IntOpenHashMap());
            }
        }

        synchronized (object2objectOverlap) {
            Int2IntMap overlaps = object2objectOverlap
                    .get(relation);
            if (overlaps == null) {
                object2objectOverlap.put(relation,
                        new Int2IntOpenHashMap());
            }
        }

        size++;
        return (true);
    }
}
