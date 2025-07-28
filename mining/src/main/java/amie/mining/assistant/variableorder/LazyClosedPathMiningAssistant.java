package amie.mining.assistant.variableorder;

import amie.data.AbstractKB;
import amie.mining.assistant.LazyMiningAssistant;
import amie.mining.assistant.MiningOperator;
import amie.rules.Rule;
import it.unimi.dsi.fastutil.ints.IntList;

import java.util.Collection;

public class LazyClosedPathMiningAssistant extends LazyMiningAssistant {
    public LazyClosedPathMiningAssistant(AbstractKB dataSource, VariableOrder order) {
        super(dataSource, order);
    }

    public LazyClosedPathMiningAssistant(AbstractKB dataSource) {
        super(dataSource);
    }

    @MiningOperator(name = "closing")
    public void getClosingAtoms(Rule rule, double minSupportThreshold, Collection<Rule> output) {
        if (rule.isClosed())
            return;
        super.getClosingAtoms(rule, minSupportThreshold, output);
    }

    @MiningOperator(name = "dangling")
    public void getDanglingAtoms(Rule rule, double minSupportThreshold, Collection<Rule> output) {
       if (rule.isEmpty() || rule.isClosed())
           return;
       super.getDanglingAtoms(rule, minSupportThreshold, output);
    }
}
