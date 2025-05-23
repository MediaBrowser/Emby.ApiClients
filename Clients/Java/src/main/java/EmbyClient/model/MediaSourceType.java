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
 * Gets or Sets MediaSourceType
 */
@JsonAdapter(MediaSourceType.Adapter.class)
public enum MediaSourceType {
  DEFAULT("Default"),
  GROUPING("Grouping"),
  PLACEHOLDER("Placeholder");

  private String value;

  MediaSourceType(String value) {
    this.value = value;
  }

  public String getValue() {
    return value;
  }

  @Override
  public String toString() {
    return String.valueOf(value);
  }

  public static MediaSourceType fromValue(String input) {
    for (MediaSourceType b : MediaSourceType.values()) {
      if (b.value.equals(input)) {
        return b;
      }
    }
    return null;
  }

  public static class Adapter extends TypeAdapter<MediaSourceType> {
    @Override
    public void write(final JsonWriter jsonWriter, final MediaSourceType enumeration) throws IOException {
      jsonWriter.value(String.valueOf(enumeration.getValue()));
    }

    @Override
    public MediaSourceType read(final JsonReader jsonReader) throws IOException {
      Object value = jsonReader.nextString();
      return MediaSourceType.fromValue((String)(value));
    }
  }
}
