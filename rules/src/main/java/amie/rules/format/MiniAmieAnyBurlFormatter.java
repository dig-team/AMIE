package amie.rules.format;

public class MiniAmieAnyBurlFormatter extends AnyBurlFormatter {

    public MiniAmieAnyBurlFormatter(boolean verbose) {
        super(verbose);
    }

    @Override
    public OutputColumn[] columns() {
        return new OutputColumn[] { OutputColumn.PcaBodySize, OutputColumn.ApproxSupport,
                OutputColumn.PcaConfEstimation, OutputColumn.Rule };
    }
}
