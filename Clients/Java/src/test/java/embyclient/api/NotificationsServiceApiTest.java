/*
 * Emby Server REST API
 * 
 */

package embyclient.api;

import embyclient.model.ApiAddAdminNotification;
import embyclient.model.NotificationCategoryInfo;
import org.junit.Test;
import org.junit.Ignore;


import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;


/**
 * API tests for NotificationsServiceApi
 */
@Ignore
public class NotificationsServiceApiTest {

    private final NotificationsServiceApi api = new NotificationsServiceApi();

    /**
     * Gets notification types
     *
     * Requires authentication as user
     *
     * @throws Exception
     *          if the Api call fails
     */
    @Test
    public void getNotificationsTypesTest() throws Exception {
        List<NotificationCategoryInfo> response = api.getNotificationsTypes();

        // TODO: test validations
    }
    /**
     * Sends a notification to all admin users
     *
     * Requires authentication as user
     *
     * @throws Exception
     *          if the Api call fails
     */
    @Test
    public void postNotificationsAdminTest() throws Exception {
        ApiAddAdminNotification body = null;
        String name = null;
        String description = null;
        String imageUrl = null;
        String url = null;
        String level = null;
        api.postNotificationsAdmin(body, name, description, imageUrl, url, level);

        // TODO: test validations
    }
}
