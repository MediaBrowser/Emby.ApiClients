/*
 * Emby Server REST API
 * 
 */

package embyclient.model;

import java.util.Objects;
import java.util.Arrays;
import com.google.gson.annotations.SerializedName;
import java.io.IOException;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;

/**
 * Gets or Sets SyncJobStatus
 */
@JsonAdapter(SyncJobStatus.Adapter.class)
public enum SyncJobStatus {
  QUEUED("Queued"),
  CONVERTING("Converting"),
  READYTOTRANSFER("ReadyToTransfer"),
  TRANSFERRING("Transferring"),
  COMPLETED("Completed"),
  COMPLETEDWITHERROR("CompletedWithError"),
  FAILED("Failed");

  private String value;

  SyncJobStatus(String value) {
    this.value = value;
  }

  public String getValue() {
    return value;
  }

  @Override
  public String toString() {
    return String.valueOf(value);
  }

  public static SyncJobStatus fromValue(String input) {
    for (SyncJobStatus b : SyncJobStatus.values()) {
      if (b.value.equals(input)) {
        return b;
      }
    }
    return null;
  }

  public static class Adapter extends TypeAdapter<SyncJobStatus> {
    @Override
    public void write(final JsonWriter jsonWriter, final SyncJobStatus enumeration) throws IOException {
      jsonWriter.value(String.valueOf(enumeration.getValue()));
    }

    @Override
    public SyncJobStatus read(final JsonReader jsonReader) throws IOException {
      Object value = jsonReader.nextString();
      return SyncJobStatus.fromValue((String)(value));
    }
  }
}
