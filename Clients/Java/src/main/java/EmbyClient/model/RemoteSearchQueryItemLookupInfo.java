/*
 * Emby Server REST API
 * 
 */

package embyclient.model;

import java.util.Objects;
import java.util.Arrays;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import embyclient.model.ItemLookupInfo;
import io.swagger.v3.oas.annotations.media.Schema;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
/**
 * RemoteSearchQueryItemLookupInfo
 */


public class RemoteSearchQueryItemLookupInfo {
  @SerializedName("SearchInfo")
  private ItemLookupInfo searchInfo = null;

  @SerializedName("ItemId")
  private Long itemId = null;

  @SerializedName("SearchProviderName")
  private String searchProviderName = null;

  @SerializedName("Providers")
  private List<String> providers = null;

  @SerializedName("IncludeDisabledProviders")
  private Boolean includeDisabledProviders = null;

  public RemoteSearchQueryItemLookupInfo searchInfo(ItemLookupInfo searchInfo) {
    this.searchInfo = searchInfo;
    return this;
  }

   /**
   * Get searchInfo
   * @return searchInfo
  **/
  @Schema(description = "")
  public ItemLookupInfo getSearchInfo() {
    return searchInfo;
  }

  public void setSearchInfo(ItemLookupInfo searchInfo) {
    this.searchInfo = searchInfo;
  }

  public RemoteSearchQueryItemLookupInfo itemId(Long itemId) {
    this.itemId = itemId;
    return this;
  }

   /**
   * Get itemId
   * @return itemId
  **/
  @Schema(description = "")
  public Long getItemId() {
    return itemId;
  }

  public void setItemId(Long itemId) {
    this.itemId = itemId;
  }

  public RemoteSearchQueryItemLookupInfo searchProviderName(String searchProviderName) {
    this.searchProviderName = searchProviderName;
    return this;
  }

   /**
   * Get searchProviderName
   * @return searchProviderName
  **/
  @Schema(description = "")
  public String getSearchProviderName() {
    return searchProviderName;
  }

  public void setSearchProviderName(String searchProviderName) {
    this.searchProviderName = searchProviderName;
  }

  public RemoteSearchQueryItemLookupInfo providers(List<String> providers) {
    this.providers = providers;
    return this;
  }

  public RemoteSearchQueryItemLookupInfo addProvidersItem(String providersItem) {
    if (this.providers == null) {
      this.providers = new ArrayList<>();
    }
    this.providers.add(providersItem);
    return this;
  }

   /**
   * Get providers
   * @return providers
  **/
  @Schema(description = "")
  public List<String> getProviders() {
    return providers;
  }

  public void setProviders(List<String> providers) {
    this.providers = providers;
  }

  public RemoteSearchQueryItemLookupInfo includeDisabledProviders(Boolean includeDisabledProviders) {
    this.includeDisabledProviders = includeDisabledProviders;
    return this;
  }

   /**
   * Get includeDisabledProviders
   * @return includeDisabledProviders
  **/
  @Schema(description = "")
  public Boolean isIncludeDisabledProviders() {
    return includeDisabledProviders;
  }

  public void setIncludeDisabledProviders(Boolean includeDisabledProviders) {
    this.includeDisabledProviders = includeDisabledProviders;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    RemoteSearchQueryItemLookupInfo remoteSearchQueryItemLookupInfo = (RemoteSearchQueryItemLookupInfo) o;
    return Objects.equals(this.searchInfo, remoteSearchQueryItemLookupInfo.searchInfo) &&
        Objects.equals(this.itemId, remoteSearchQueryItemLookupInfo.itemId) &&
        Objects.equals(this.searchProviderName, remoteSearchQueryItemLookupInfo.searchProviderName) &&
        Objects.equals(this.providers, remoteSearchQueryItemLookupInfo.providers) &&
        Objects.equals(this.includeDisabledProviders, remoteSearchQueryItemLookupInfo.includeDisabledProviders);
  }

  @Override
  public int hashCode() {
    return Objects.hash(searchInfo, itemId, searchProviderName, providers, includeDisabledProviders);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class RemoteSearchQueryItemLookupInfo {\n");
    
    sb.append("    searchInfo: ").append(toIndentedString(searchInfo)).append("\n");
    sb.append("    itemId: ").append(toIndentedString(itemId)).append("\n");
    sb.append("    searchProviderName: ").append(toIndentedString(searchProviderName)).append("\n");
    sb.append("    providers: ").append(toIndentedString(providers)).append("\n");
    sb.append("    includeDisabledProviders: ").append(toIndentedString(includeDisabledProviders)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(java.lang.Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }

}
